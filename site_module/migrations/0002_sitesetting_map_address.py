# Generated by Django 5.0 on 2024-09-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='map_address',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='لینک مشاهده آدرس در map'),
        ),
    ]
