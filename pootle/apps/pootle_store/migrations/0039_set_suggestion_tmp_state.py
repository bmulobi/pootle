# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 05:28
from __future__ import unicode_literals

from django.db import migrations
from django.db.models import F


def set_suggestion_tmp(apps, schema_editor):
    suggestions = apps.get_model("pootle_store.Suggestion").objects.all()
    suggestions.update(tmp_state=F("state"))


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_store', '0038_suggestion_tmp_state'),
    ]

    operations = [
        migrations.RunPython(set_suggestion_tmp),
    ]
