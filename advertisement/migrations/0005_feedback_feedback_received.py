# Generated by Django 5.2.1 on 2025-05-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0004_alter_advertisement_text_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='feedback_received',
            field=models.BooleanField(default=False),
        ),
    ]
