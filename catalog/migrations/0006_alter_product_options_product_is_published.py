# Generated by Django 4.2.6 on 2023-11-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('price',), 'permissions': [('product_published', 'Can publish product')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликован'),
        ),
    ]