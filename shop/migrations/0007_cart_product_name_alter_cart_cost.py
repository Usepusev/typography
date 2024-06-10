# Generated by Django 4.2.13 on 2024-06-09 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]