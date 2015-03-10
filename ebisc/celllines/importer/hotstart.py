import os
import csv

import logging
logger = logging.getLogger('management.commands')

from ..models import *


'''
+ binnedage.txt'
R cellline.txt'
R celllinechecklist.txt' (cellline)
R celllinelab.txt' (cellline)
R celllineorganization.txt' (cellline)
+ celllinestatus.txt'
? celllineuse.txt'
+ celltype.txt'
+ country.txt'
+ culturesystem.txt'
+ disease.txt'
? diseasearea.txt'
R document.txt'
R donor.txt'
+ gender.txt'
R organization.txt'
+ phenotype.txt'
+ phonecountrycode.txt'
+ reprogmethod1.txt'
+ reprogmethod2.txt'
+ reprogmethod3.txt'
? treatmentbeforecollection.txt'
'''

FILES = [
    {
        'filename': 'disease.txt',
        'model': Disease,
        'fields': {'id': 0, 'disease': 1}
    },
    {
        'filename': 'binnedage.txt',
        'model': Binnedage,
        'fields': {'id': 0, 'binnedage': 1}
    },
    {
        'filename': 'celllinestatus.txt',
        'model': Celllinestatus,
        'fields': {'id': 0, 'celllinestatus': 1}
    },
    {
        'filename': 'celltype.txt',
        'model': Celltype,
        'fields': {'id': 0, 'celltype': 1}
    },
    {
        'filename': 'country.txt',
        'model': Country,
        'fields': {'id': 0, 'country': 1}
    },
    {
        'filename': 'culturesystem.txt',
        'model': Culturesystem,
        'fields': {'id': 0, 'culturesystem': 1}
    },
    {
        'filename': 'gender.txt',
        'model': Gender,
        'fields': {'id': 0, 'gender': 1}
    },
    {
        'filename': 'organization.txt',
        'model': Organization,
        'fields': {'id': 0, 'organizationshortname': 1}
    },
    {
        'filename': 'phenotype.txt',
        'model': Phenotype,
        'fields': {'id': 0, 'phenotype': 1}
    },
    {
        'filename': 'phonecountrycode.txt',
        'model': Phonecountrycode,
        'fields': {'id': 0, 'phonecountrycode': 1}
    },
    {
        'filename': 'reprogmethod1.txt',
        'model': Reprogrammingmethod1,
        'fields': {'id': 0, 'reprogrammingmethod1': 1}
    },
    {
        'filename': 'reprogmethod2.txt',
        'model': Reprogrammingmethod2,
        'fields': {'id': 0, 'reprogrammingmethod2': 1}
    },
    {
        'filename': 'reprogmethod3.txt',
        'model': Reprogrammingmethod3,
        'fields': {'id': 0, 'reprogrammingmethod3': 1}
    },
]


def import_hotstart(basedir):

    for f in FILES:
        logger.info('Importing %s' % f['filename'])

        f['model'].objects.all().delete()

        with open(os.path.join(basedir, f['filename']), 'r') as fi:

            reader = csv.reader(fi)
            next(reader, None)

            for line in reader:
                logger.debug('  Data: %s' % line)

                kwargs = {}
                for key, value in f['fields'].items():
                    kwargs[key] = line[value]
                logger.debug('  Args: %s' % kwargs)

                obj = f['model'](**kwargs)
                obj.save()
                logger.debug('  Object: %s' % obj)
