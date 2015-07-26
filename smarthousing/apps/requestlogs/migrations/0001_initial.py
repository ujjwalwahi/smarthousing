# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('host', models.CharField(max_length=1000)),
                ('path', models.CharField(max_length=1000)),
                ('method', models.CharField(max_length=50)),
                ('uri', models.CharField(max_length=2000)),
                ('status_code', models.IntegerField()),
                ('user_agent', models.CharField(max_length=1000, null=True, blank=True)),
                ('remote_addr', models.IPAddressField()),
                ('remote_addr_fwd', models.IPAddressField(null=True, blank=True)),
                ('meta', models.TextField()),
                ('cookies', models.TextField(null=True, blank=True)),
                ('get', models.TextField(null=True, blank=True)),
                ('post', models.TextField(null=True, blank=True)),
                ('raw_post', models.TextField(null=True, blank=True)),
                ('is_secure', models.BooleanField()),
                ('is_ajax', models.BooleanField()),
            ],
        ),
    ]
