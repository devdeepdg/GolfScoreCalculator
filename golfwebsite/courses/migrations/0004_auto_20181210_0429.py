# Generated by Django 2.1.3 on 2018-12-10 04:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20181210_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='par',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=None),
        ),
    ]
