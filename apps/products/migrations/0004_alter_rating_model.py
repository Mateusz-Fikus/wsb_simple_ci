# Generated by Django 3.2.3 on 2022-01-03 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220103_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='products.product'),
        ),
    ]