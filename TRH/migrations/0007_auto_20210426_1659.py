# Generated by Django 3.1.6 on 2021-04-26 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TRH', '0006_auto_20210426_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='admitquant',
            new_name='admit',
        ),
    ]
