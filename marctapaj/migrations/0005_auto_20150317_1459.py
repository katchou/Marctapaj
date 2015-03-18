# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('marctapaj', '0004_auto_20150317_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 17, 13, 59, 57, 668779, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
