# Generated by Django 3.2.6 on 2021-11-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='invited_peaple',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='ranking',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='sum_of_trades',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='verified_trades',
            field=models.IntegerField(default=0),
        ),
    ]