# Generated by Django 3.1.7 on 2021-03-12 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210228_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('is_inf_swipes', models.BooleanField()),
                ('swipe_count', models.IntegerField()),
                ('default_radius', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='subscription_type',
        ),
        migrations.CreateModel(
            name='CustomRadius',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radius', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
