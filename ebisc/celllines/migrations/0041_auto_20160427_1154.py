# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celllines', '0040_celllinealiquot_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellline',
            name='availability',
            field=models.CharField(default=b'not_available', max_length=30, verbose_name='Availability', choices=[(b'not_available', 'Not available'), (b'at_ecacc', 'Stocked by ECACC'), (b'expand_to_order', 'Expand to order'), (b'restricted_distribution', 'Restricted distribution')]),
        ),
    ]
