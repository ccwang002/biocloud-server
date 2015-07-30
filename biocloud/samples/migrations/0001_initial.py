# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import samples.models
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=2048)),
                ('sample_file', models.FileField(blank=True, max_length=1024, upload_to=samples.models.Sample.temp_upload_to)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='owned_samples')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
