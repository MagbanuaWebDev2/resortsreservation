# Generated by Django 3.1.6 on 2021-05-15 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrance', models.TextField(choices=[('Day', 'Day'), ('Night', 'Night'), ('Overnight', 'Overnight')])),
                ('admit', models.IntegerField(default='1')),
            ],
        ),
        migrations.CreateModel(
            name='Cottage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cottage', models.TextField(choices=[('Small Kubo [5 pax]', 'Small Kubo [5 pax]'), ('Big Kubo [10 pax]', 'Big Kubo [10 pax]'), ('Cavana [11-20 pax]', 'Cavana [11-20 pax]'), ('Full Cavana [30 pax]', 'Full Cavana [30 pax]')])),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('contact', models.CharField(max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort', models.TextField(choices=[('Tubigan Garden Resort', 'Tubigan'), ('Saniya Resort & Hotel', 'Saniya'), ('Coco Valley Richnez Waterpark', 'Coco Valley'), ('Volets Hotel & Resort', 'Volets')], default='none')),
                ('admission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='TRH.admission')),
                ('cottage', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='TRH.cottage')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserve', models.DateField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TRH.customer')),
                ('resortchosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TRH.resort')),
            ],
        ),
    ]
