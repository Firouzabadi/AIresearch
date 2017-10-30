# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mnistimage',
            fields=[
                ('imageid', models.AutoField(primary_key=True, serialize=False)),
                ('trained_label', models.IntegerField(choices=[(0, 'even'), (1, 'odd')])),
                ('predicted_label', models.CharField(choices=[(0, 'even'), (1, 'odd')], max_length=200)),
                ('file_address', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='MNIST_images')),
            ],
        ),
    ]