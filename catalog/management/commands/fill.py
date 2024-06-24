import json
import os.path

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('D:\Glazunov Py\dz_Django1\catalog_data_category.json', 'r') as file:
            category_data = json.load(file)
        return category_data

    @staticmethod
    def json_read_products():
        with open('D:\Glazunov Py\dz_Django1\catalog_data_product.json', 'r') as file:
            product_data = json.load(file)
        return product_data

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['fields']['name'], description=category['fields']['description'])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product['fields']['name'], description=product['fields']['description'],
                        image=product['fields']['image'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'],
                        create_at=product['fields']['create_at'],
                        updated_at=product['fields']['updated_at']))

        Product.objects.bulk_create(product_for_create)
