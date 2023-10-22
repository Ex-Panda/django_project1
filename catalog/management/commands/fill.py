from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name_category': 'Молочные продукты', 'description_category': 'Йогурты, творог, сметана'},
            {'name_category': 'Выпечка', 'description_category': 'Хлеб, булочки'},
            {'name_category': 'Для дома', 'description_category': 'Ковры, цветы, швабры'},
            {'name_category': 'Сантехника', 'description_category': 'Трубы, краны, смесители'}
        ]
        product_list = [
            {'name_product': 'Йогурт', 'description_product': 'Вкусный молочный', 'image_product': '',
             'category_product': 'Молочные продукты', 'price': '100', 'date_creation': '2023-10-11T11:50:15Z',
             'last_modified_date': '2023-10-11T14:20:19Z'},
            {'name_product': 'Хлеб', 'description_product': 'Свежий', 'image_product': '',
             'category_product': 'Выпечка', 'price': '40', 'date_creation': '2023-12-12T12:50:15Z',
             'last_modified_date': '2023-12-12T19:20:19Z'},
            {'name_product': 'Ковер', 'description_product': 'Красивый', 'image_product': '',
             'category_product': 'Для дома', 'price': '700', 'date_creation': '2022-12-11T15:55:15Z',
             'last_modified_date': '2023-10-11T14:20:19Z'},
            {'name_product': 'Смеситель', 'description_product': 'Надежный качественный', 'image_product': '',
             'category_product': 'Сантехника', 'price': '500', 'date_creation': '2023-11-11T16:30:15Z',
             'last_modified_date': '2023-11-12T18:20:19Z'}
        ]
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )

        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)

        Product.objects.all().delete()
        Product.objects.bulk_create(product_for_create)
