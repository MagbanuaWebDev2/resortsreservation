# Generated by Django 3.1.6 on 2021-06-20 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRH', '0006_auto_20210619_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='prkamnt',
            field=models.IntegerField(null=True),
        ),
    ]
