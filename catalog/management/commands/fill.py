from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name_category': 'Молочные продукты', 'description_category': 'Йогурты, творог, сметана'},
            {'name_category': 'Выпечка', 'description_category': 'Хлеб, булочки'},
            {'name_category': 'Для дома', 'description_category': 'Ковры, цветы, швабры'},
            {'name_category': 'Сантехника', 'description_category': 'Трубы, краны, смесители'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)
