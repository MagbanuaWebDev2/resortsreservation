# Generated by Django 3.1.6 on 2021-05-30 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRH', '0011_auto_20210530_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='entrance',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cottage',
            name='cottage',
            field=models.CharField(max_length=100),
        ),
    ]
