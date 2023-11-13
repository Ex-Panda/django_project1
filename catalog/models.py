import datetime

from django.db import models

from user_auth.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='наименование продукта')
    description_product = models.CharField(max_length=200, verbose_name='описание продукта')
    image_product = models.ImageField(upload_to='products/', verbose_name='изображение продукта', **NULLABLE)
    category_product = models.CharField(max_length=100, verbose_name='наименование категории продукта')
    price = models.IntegerField(verbose_name='цена продукта')
    date_creation = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    last_modified_date = models.DateTimeField(verbose_name='дата последнего изменения', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f"""{self.name_product} {self.description_product} {self.price} {self.category_product}"""

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('price',)


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='наименование категории')
    description_category = models.CharField(max_length=200, verbose_name='описание категории')

    def __str__(self):
        return f"{self.id} {self.name_category}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name_category',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(max_length=50, verbose_name='номер версии', default=1)
    name_version = models.CharField(max_length=100, verbose_name='название версии')
    sing_version = models.BooleanField(verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product} {self.name_version}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
