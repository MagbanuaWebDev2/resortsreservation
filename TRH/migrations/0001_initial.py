# Generated by Django 3.1.6 on 2021-06-13 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.CharField(max_length=50, null=True)),
                ('cardnum', models.CharField(max_length=20, null=True)),
                ('expmonth', models.CharField(max_length=8, null=True)),
                ('expyear', models.CharField(max_length=4, null=True)),
                ('code', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100)),
                ('card', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='TRH.card')),
            ],
        ),
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserve', models.DateField()),
                ('tot_amount', models.IntegerField(default='0')),
                ('request', models.TextField()),
                ('customer', models.ManyToManyField(to='TRH.Customer')),
                ('resortchosen', models.ManyToManyField(to='TRH.Resort')),
            ],
        ),
        migrations.CreateModel(
            name='Cottage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cottage', models.CharField(max_length=100)),
                ('quant', models.IntegerField()),
                ('priceb', models.IntegerField()),
                ('resorts', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='TRH.resort')),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrance', models.CharField(max_length=30)),
                ('admit', models.IntegerField(default='1')),
                ('pricea', models.IntegerField(default='100')),
                ('resorts', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='TRH.resort')),
            ],
        ),
    ]
