# Generated by Django 5.0 on 2024-09-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0005_alter_user_email_active_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reset_code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='کد بازیابی کلمه عبور'),
        ),
    ]
