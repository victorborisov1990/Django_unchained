from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from random import randint, uniform, choice

from market.models import ProductsModel


class Command(BaseCommand):
    products = ['Сыр твёрдый', 'Перец чёрный молотый', 'Масло растительное', 'Чеснок', 'картошка', 'макароны',
                'морковь', 'гречка', 'мука', 'вода', 'майонез']
    def handle(self, *args, **kwargs):
        product_list = Command.products.copy()
        for i in range(0, 10):
            item = choice(product_list)
            product_list.remove(item)
            product = ProductsModel(name=f'{item} {i}',
                                   description=lorem_ipsum.paragraph(),
                                   price=uniform(1, 1000),
                                   quantity=randint(0, 100),
                                   )
            product.save()
            print(f'Создан продукт: {product}')
