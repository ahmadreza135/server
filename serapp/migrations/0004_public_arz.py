# Generated by Django 3.2.6 on 2021-10-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serapp', '0003_delete_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='public_arz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('timeopened', models.DateTimeField(default='1998')),
                ('timeclosing', models.DateTimeField(default='2000')),
                ('market_cap', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
