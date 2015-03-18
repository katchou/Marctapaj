# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('marctapaj', '0003_auto_20150301_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='last_access',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 17, 13, 59, 3, 482680, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
