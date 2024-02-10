from django.core.management.base import BaseCommand
from random import choice, randint
from market.models import ClientsModel, ProductsModel, OrdersModel


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        products = ProductsModel.objects.all()
        for _ in range(0, 10):
            clients = ClientsModel.objects.all()
            product_list = list(products)
            num_of_products = randint(1, len(product_list)) # число продуктов в заказе (но не больше ассортимента)
            products_in_order = []
            # product = choice(product_list)  # создаем заказ с одним товаром
            # product_list.remove(product)
            order = OrdersModel.objects.create(client=choice(clients))
            total_price = 0
            for _ in range(0, num_of_products):  # создаем список со случайными оставшимися продуктами
                product = choice(product_list)
                product_list.remove(product)
                products_in_order.append(product)
                total_price += product.price
            order.product.add(*products_in_order)
            # order.product.set(products_in_order)
            order.amount += total_price
            order.save()
            print(f'Создан заказ: {order} ')

