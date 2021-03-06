# Generated by Django 3.1.7 on 2021-03-04 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geodata',
            name='appointment_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='geodata',
            name='latitude',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='geodata',
            name='longitude',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
