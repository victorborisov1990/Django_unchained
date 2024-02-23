from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from random import randint, uniform

from market.models import ProductsModel


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(0, 5):
            product = ProductsModel(name=f'name{i}',
                                   description=lorem_ipsum.paragraph(),
                                   price=uniform(1, 1000),
                                   quantity=randint(0, 100),
                                   )
            product.save()
            print(f'Создан продукт: {product}')
