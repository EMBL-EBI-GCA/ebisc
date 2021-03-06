import os
import hashlib
import requests
from easydict import EasyDict as ToObject

import logging
logger = logging.getLogger('management.commands')

from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from ebisc.celllines.models import CelllineBatch, BatchCultureConditions, CelllineBatchImages, CelllineInformationPack


'''
LIMS batch data importer.
'''


# -----------------------------------------------------------------------------
#  Run

def run():

    for lims_batch in query(settings.LIMS.get('url')):

        logger.info('Processing batch {} for cell line {}'.format(lims_batch.batch_id, lims_batch.cell_line))

        lims_batch_data = query(lims_batch.href)

        if not lims_batch_data.biosamples_batch_id:
            logger.warn('Missing biosamples ID ... skipping batch')
            continue

        try:
            batch = CelllineBatch.objects.get(biosamples_id=lims_batch_data.biosamples_batch_id)
            batch.batch_id = lims_batch_data.batch_id

            # Inventory

            if 'vials_at_roslin' in lims_batch_data:
                batch.vials_at_roslin = value_of_int(lims_batch_data.vials_at_roslin)

            if 'vials_shipped_to_ECACC' in lims_batch_data:
                batch.vials_shipped_to_ecacc = value_of_int(lims_batch_data.vials_shipped_to_ECACC)

            if 'vials_shipped_to_fraunhoffer' in lims_batch_data:
                batch.vials_shipped_to_fraunhoffer = value_of_int(lims_batch_data.vials_shipped_to_fraunhoffer)

            batch.save()

            # Certificate of analysis
            if 'certificate_of_analysis' in lims_batch_data:
                batch.certificate_of_analysis_md5 = value_of_file(
                    lims_batch_data.certificate_of_analysis.file,
                    batch.certificate_of_analysis,
                    source_md5=lims_batch_data.certificate_of_analysis.md5,
                    current_md5=batch.certificate_of_analysis_md5,
                )
                batch.save()

            # Images

            old_images = set([img.md5 for img in batch.images.all()])
            if 'images' in lims_batch_data:
                new_images = set([img.md5 for img in lims_batch_data.images])
            else:
                new_images = set()

            # Delete old images that are not in new images

            for img_md5 in old_images - new_images:
                logger.info('Deleting old image')
                batch.images.filter(md5=img_md5).delete()

            # Add new images

            if len(new_images - old_images) > 0:
                for image in lims_batch_data.images:
                    if image.md5 in (new_images - old_images):
                        batch_image = CelllineBatchImages(
                            batch=batch,
                            magnification=image.magnification,
                            time_point=image.timepoint,
                        )
                        batch_image.save()

                        filename, file_extension = os.path.splitext(image.file)

                        batch_image.md5 = value_of_file(
                            image.file,
                            batch_image.image,
                            filename='%s-%s.%s' % (lims_batch.cell_line, hashlib.md5(os.path.basename(image.file)).hexdigest(), file_extension),
                            source_md5=image.md5,
                            current_md5=batch_image.md5,
                        )
                        batch_image.save()

            # Culture conditions

            if 'culture_conditions' in lims_batch_data:
                culture_conditions, created = BatchCultureConditions.objects.get_or_create(batch=batch)

                culture_conditions.culture_medium = lims_batch_data.culture_conditions.medium
                culture_conditions.matrix = lims_batch_data.culture_conditions.matrix
                culture_conditions.passage_method = lims_batch_data.culture_conditions.passage_method
                culture_conditions.o2_concentration = lims_batch_data.culture_conditions.O2_concentration
                culture_conditions.co2_concentration = lims_batch_data.culture_conditions.CO2_concentration
                culture_conditions.temperature = lims_batch_data.culture_conditions.temperature

                if created or culture_conditions.is_dirty():
                    if created:
                        logger.info('Created new batch culture conditions')
                    else:
                        logger.info('Updated batch culture conditions')

                    culture_conditions.save()

        except CelllineBatch.DoesNotExist:
            logger.warn('Unknown batch with biosamples ID = {}'.format(lims_batch_data.biosamples_batch_id))


# -----------------------------------------------------------------------------
#  Utils

def query(url):
    return ToObject(requests.get(url, auth=(settings.LIMS.get('username'), settings.LIMS.get('password'))).json()).data


def value_of_int(value):

    if value == '':
        return None

    return value


def value_of_file(value, file_field, filename=None, source_md5=None, current_md5=None):

    # Save file for file_field and return its md5

    if value == '':
        file_field.delete()
        return None

    if filename is None:
        source_filename = os.path.basename(value)
    else:
        source_filename = filename

    current_filename = os.path.basename(file_field.name)

    if source_md5 is not None and current_md5 is not None and source_md5 == current_md5 and source_filename == current_filename:
        return current_md5

    logger.info('Fetching data file from %s' % value)

    response = requests.get(value, stream=True, auth=(settings.LIMS.get('username'), settings.LIMS.get('password')))

    with NamedTemporaryFile(delete=True) as f:
        for chunk in response.iter_content(10240):
            f.write(chunk)

        f.seek(0)
        file_field.save(source_filename, File(f), save=False)
        file_field.instance.save()

        f.seek(0)
        return hashlib.md5(f.read()).hexdigest()

# -----------------------------------------------------------------------------
