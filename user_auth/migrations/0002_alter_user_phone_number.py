# Generated by Django 4.2.6 on 2023-11-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=20, null=True, verbose_name='phone number'),
        ),
    ]
