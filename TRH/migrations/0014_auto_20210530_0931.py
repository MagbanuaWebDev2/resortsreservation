# Generated by Django 3.1.6 on 2021-05-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRH', '0013_auto_20210530_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='entrance',
            field=models.CharField(max_length=30),
        ),
    ]
