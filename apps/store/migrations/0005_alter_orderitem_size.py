# Generated by Django 3.2.3 on 2022-01-06 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_total_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='size',
            field=models.IntegerField(),
        ),
    ]
