from django.core.management.base import BaseCommand
from random import randint
from market.models import ClientsModel


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for i in range(0, 5):
            client = ClientsModel(name=f'Имя{i}',
                                  email=f'author{i}@mail.ru',
                                  phone=str(randint(1_000_000, 9_999_999)),
                                  address=f'address{i}',
                                  )
            client.save()
            print(f'Создан Клиент: {client} ')
