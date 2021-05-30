# Generated by Django 3.1.6 on 2021-05-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRH', '0009_auto_20210530_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cottage',
            name='cottage',
            field=models.CharField(choices=[('1', 'Small Kubo (6 pax)'), ('2', 'Medium Kubo (12 pax)'), ('3', 'Large Kubo (15 pax)'), ('4', 'Open Kubo (20 pax)'), ('5', 'Gazebo (9 pax)'), ('6', 'Gazebo (4 pax)'), ('7', 'Small Kubo (8 pax)'), ('8', 'Medium Kubo (10 pax)'), ('9', 'Large Kubo (15 pax)'), ('10', 'Peach Cottage (10 pax)'), ('11', 'Violet Cottage (25 pax)'), ('12', 'Small Kubo (5 pax)'), ('13', 'Big Kubo (8-10 pax)'), ('14', 'Small Cavana (8 pax)'), ('15', 'Kubo Cavana (10-12 pax)'), ('16', 'Full Cavana (20 pax)'), ('17', 'Umbrella (4 pax)'), ('18', 'Short Table (6 pax)'), ('19', 'Petits Cottage (10 pax)'), ('20', 'Grande Cottage (20 pax)'), ('21', 'Big Nipa Hut (30 pax)'), ('22', 'Regular Cottage (10 pax)'), ('23', 'Big Cottage (25 pax)'), ('24', 'Bahay Kubo (2 pax)'), ('25', 'Regular Cottage (10 pax)'), ('26', 'Regular Cottage (16 pax)'), ('27', 'Small Kubo (8 pax)'), ('28', 'Big Kubo (10 pax)'), ('29', 'Tent (6 pax)'), ('30', 'Table with Umbrella (4 pax)'), ('31', 'Regular Cottage (15-20 pax)'), ('32', 'Table (8-10 pax)'), ('33', 'Umbrella (4 pax)'), ('34', 'Family Kubo (20 pax)'), ('35', 'Kubo with sink (12 pax)'), ('36', 'Table (6 pax)'), ('37', 'Regular Cottage (8 pax)'), ('38', 'Regular Cottage (12 pax)'), ('39', 'Regular Cottage (15 pax)'), ('40', 'Gazebo Kubo (15 pax)'), ('41', 'Elevated Floor (20 pax)')], max_length=100),
        ),
    ]
