import csv
import sys

from ebisc.celllines.models import Cellline


'''Export temporary CSV for ECACC'''


# -----------------------------------------------------------------------------
#  Run

def run():

    writer = csv.writer(sys.stdout, dialect=csv.excel_tab)

    writer.writerow((
        'biosamples_id',

        'name',
        'alternative_names',

        'depositor',

        'donor_biosamples_id',
        'donor_gender',
        'donor_age',

        'primary_disease_doid',
        'primary_disease_name',
        'primary_disease_synonyms',

        'cell_type',
        'karyotype',

        'reprogramming_method_type',
        'reprogramming_method_vector',
        'reprogramming_method_virus',
        'reprogramming_method_transposon',
        'reprogramming_method_excisable',
        'reprogramming_method_absence_reprogramming_vectors',

        'culture_conditions_culture_medium',
        'culture_conditions_passage_method',
        'culture_conditions_surface_coating',
        'culture_conditions_co2_concentration',
        'culture_conditions_o2_concentration',

        'pubmed_url',
        'pubmed_title',
    ))

    for cl in Cellline.objects.all():

        if hasattr(cl, 'integrating_vector'):
            reprogramming_method = [
                'integrating',
                cl.integrating_vector.vector,
                cl.integrating_vector.virus,
                cl.integrating_vector.transposon,
                cl.integrating_vector.excisable,
                cl.integrating_vector.absence_reprogramming_vectors,
            ]
        elif hasattr(cl, 'non_integrating_vector'):
            reprogramming_method = [
                'non-integrating',
                cl.non_integrating_vector.vector,
                None, None, None
            ]
        else:
            reprogramming_method = [None, None, None, None, None]

        writer.writerow(flatten((
            cl.biosamples_id,

            cl.name,
            cl.alternative_names,

            cl.generator.name.encode('utf8'),

            cl.donor.biosamples_id,
            cl.donor.gender,
            cl.donor_age,

            cl.primary_disease.icdcode if cl.primary_disease else '',
            cl.primary_disease.disease if cl.primary_disease else 'Normal',
            cl.primary_disease.synonyms if cl.primary_disease else '',

            cl.celllinederivation.primary_cell_type.name,
            cl.karyotype if hasattr(cl, 'karyotype') and cl.karyotype else '',

            reprogramming_method,

            cl.celllinecultureconditions.culture_medium,
            cl.celllinecultureconditions.passage_method,
            cl.celllinecultureconditions.surface_coating,
            cl.celllinecultureconditions.co2_concentration,
            cl.celllinecultureconditions.o2_concentration,

            cl.publications.all()[0].reference_url if cl.publications.all().count() else '',
            cl.publications.all()[0].reference_title.encode('utf8') if cl.publications.all().count() else '',
        )))


# -----------------------------------------------------------------------------
#  Utils

def flatten(lis):

    '''Given a list, possibly nested to any level, return it flattened.'''

    new_list = []

    for item in lis:
        if isinstance(item, type([])):
            new_list.extend(flatten(item))
        else:
            new_list.append(item)

    return new_list

# -----------------------------------------------------------------------------
