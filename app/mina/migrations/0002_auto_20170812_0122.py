# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("mina", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="minapost",
            options={"ordering": ("-created_date",)},
        ),
        migrations.AlterField(
            model_name="minapost",
            name="created_date",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
