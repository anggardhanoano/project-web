# Generated by Django 2.1.2 on 2018-12-14 02:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20181214_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notemodel',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
