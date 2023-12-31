# Generated by Django 4.2.6 on 2023-11-09 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения'),
        ),
    ]
