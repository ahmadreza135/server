# Generated by Django 3.2.6 on 2021-11-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('siteapp', '0002_delete_dashboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarafi', models.CharField(max_length=50)),
                ('verified_trades', models.IntegerField()),
            ],
        ),
    ]
