# Generated by Django 4.2.6 on 2023-10-19 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=100, verbose_name='наименование категории')),
                ('description_category', models.CharField(max_length=200, verbose_name='описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=100, verbose_name='наименование продукта')),
                ('description_product', models.CharField(max_length=200, verbose_name='описание продукта')),
                ('image_product', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='изображение продукта')),
                ('category_product', models.CharField(max_length=100, verbose_name='наименование категории продукта')),
                ('price', models.IntegerField(verbose_name='цена продукта')),
                ('date_creation', models.DateTimeField(verbose_name='дата создания')),
                ('last_modified_date', models.DateTimeField(verbose_name='дата последнего изменения')),
            ],
        ),
    ]
