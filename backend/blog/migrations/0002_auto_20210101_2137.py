# Generated by Django 3.0.5 on 2021-01-01 21:37

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]