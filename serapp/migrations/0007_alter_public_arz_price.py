# Generated by Django 3.2.6 on 2021-11-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serapp', '0006_alter_public_arz_market_cap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public_arz',
            name='price',
            field=models.FloatField(),
        ),
    ]