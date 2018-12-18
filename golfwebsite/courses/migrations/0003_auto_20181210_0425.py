# Generated by Django 2.1.3 on 2018-12-10 04:25

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20181210_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='par',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]), size=None),
        ),
    ]
