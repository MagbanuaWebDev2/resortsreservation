# Generated by Django 3.1.6 on 2021-06-20 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TRH', '0008_auto_20210620_0431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='request',
            new_name='suggest',
        ),
    ]
