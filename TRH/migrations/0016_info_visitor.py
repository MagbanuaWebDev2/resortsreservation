# Generated by Django 3.1.6 on 2021-04-27 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRH', '0015_remove_info_visitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='Visitor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='TRH.user'),
        ),
    ]
