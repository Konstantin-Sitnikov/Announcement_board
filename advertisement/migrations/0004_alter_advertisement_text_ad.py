# Generated by Django 5.2.1 on 2025-05-14 02:33

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_feedback_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='text_ad',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
