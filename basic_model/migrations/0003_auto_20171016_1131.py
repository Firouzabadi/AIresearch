# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_model', '0002_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mnistimage',
            name='file_address',
        ),
        migrations.AlterField(
            model_name='mnistimage',
            name='image',
            field=models.ImageField(null=True, upload_to='MNIST_images'),
        ),
        migrations.AlterField(
            model_name='mnistimage',
            name='predicted_label',
            field=models.IntegerField(choices=[(1, 'even'), (2, 'odd')]),
        ),
        migrations.AlterField(
            model_name='mnistimage',
            name='trained_label',
            field=models.IntegerField(choices=[(1, 'even'), (2, 'odd')]),
        ),
    ]