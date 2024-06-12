# Generated by Django 4.2.13 on 2024-06-12 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0010_order_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='bills/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='new', max_length=20)),
                ('order', models.ManyToManyField(to='shop.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
