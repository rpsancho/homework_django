import json
from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories(file_path):
        with open(file=file_path, mode="r", encoding="UTF-8") as f:
            data = json.load(f)
            result = []
            for item in data:
                if item['model'] == 'catalog.category':
                    result.append(item)

        return result


    @staticmethod
    def json_read_products(file_path):
        with open(file=file_path, mode="r", encoding="UTF-8") as f:
            data = json.load(f)
            result = []
            for item in data:
                if item['model'] == 'catalog.product':
                    result.append(item)

        return result


    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories("catalog_data.json"):
            category_for_create.append(
                Category(
                    name=category['fields']['name'],
                    description=category['fields']['description']
                    )
            )
        
        for product in Command.json_read_products("catalog_data.json"):
            product_for_create.append(
                Product(
                    name=product['fields']['name'],
                    description=product['fields']['description'],
                    preview=product['fields']['preview'],
                    category=product['fields']['category'],
                    price=product['fields']['price'],
                    created_at=product['fields']['created_at'],
                    updated_at=product['fields']['updated_at']
                    )
            )
        Category.objects.bulk_create(category_for_create)
        Product.objects.bulk_create(product_for_create)
