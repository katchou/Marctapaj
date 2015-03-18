# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('marctapaj', '0002_auto_20150301_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('content', models.TextField()),
                ('update_date', models.DateTimeField(default=datetime.datetime(2015, 3, 1, 19, 40, 36, 568141, tzinfo=utc))),
                ('bookmark', models.ForeignKey(to='marctapaj.Bookmark')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='bookmark',
            name='note',
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='access_count',
            field=models.IntegerField(editable=False, default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 1, 19, 40, 36, 567141, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='last_access',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 3, 1, 19, 40, 36, 567141, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
