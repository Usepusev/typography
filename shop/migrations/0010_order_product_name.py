# Generated by Django 4.2.13 on 2024-06-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_support'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]