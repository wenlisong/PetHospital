# Generated by Django 2.0.2 on 2018-03-20 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Navigation', '0001_initial'),
        ('Disease', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inhospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('in_time', models.DateTimeField(verbose_name='in time')),
                ('out_time', models.DateTimeField(verbose_name='out time')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disease.SubDisease')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=1000)),
                ('response_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Navigation.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('due_date', models.DateTimeField(verbose_name='due date')),
                ('desc', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='inhospital',
            name='response_people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manage.People'),
        ),
        migrations.AddField(
            model_name='inhospital',
            name='response_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Navigation.Room'),
        ),
        migrations.AddField(
            model_name='charge',
            name='response_people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manage.People'),
        ),
        migrations.AddField(
            model_name='charge',
            name='response_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Navigation.Room'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='response_people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manage.People'),
        ),
    ]
