# Generated by Django 3.2.6 on 2021-10-30 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serapp', '0004_public_arz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public_arz',
            name='timeclosing',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='public_arz',
            name='timeopened',
            field=models.DateTimeField(),
        ),
    ]
