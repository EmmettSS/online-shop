# Generated by Django 5.0 on 2024-09-12 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0007_productcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcomment',
            old_name='article',
            new_name='product',
        ),
    ]
