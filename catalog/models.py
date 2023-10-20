from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='наименование продукта')
    description_product = models.CharField(max_length=200, verbose_name='описание продукта')
    image_product = models.ImageField(upload_to='products/', verbose_name='изображение продукта', **NULLABLE)
    category_product = models.CharField(max_length=100, verbose_name='наименование категории продукта')
    price = models.IntegerField(verbose_name='цена продукта')
    date_creation = models.DateTimeField(verbose_name='дата создания')
    last_modified_date = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f"""{self.id} {self.name_product} {self.price} {self.category_product}"""


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='наименование категории')
    description_category = models.CharField(max_length=200, verbose_name='описание категории')

    def __str__(self):
        return f"{self.id} {self.name_category}"
