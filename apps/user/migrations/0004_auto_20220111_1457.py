# Generated by Django 3.2.3 on 2022-01-11 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220111_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]
