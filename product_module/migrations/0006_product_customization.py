# Generated by Django 5.0 on 2024-09-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_product_cpu_model_product_cpu_processor'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='customization',
            field=models.BooleanField(default=False, verbose_name='قابل کاستوم شدن'),
        ),
    ]
