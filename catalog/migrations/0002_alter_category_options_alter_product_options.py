# Generated by Django 4.2.6 on 2023-10-29 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name_category',), 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('price',), 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
