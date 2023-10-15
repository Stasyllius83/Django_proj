from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {'name': 'Песок', 'description': 'Песок белый 1т', 'category': '4', 'price': '10000', 'date': '2023-10-15',
             'last_date_chance': '2023-10-15'},
            {'name': 'Песок', 'description': 'Песок темный 1т', 'category': '4', 'price': '8000', 'date': '2023-10-15',
             'last_date_chance': '2023-10-15'}
        ]

        products_for_create = []
        for product_item in product_list:
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_for_create)
