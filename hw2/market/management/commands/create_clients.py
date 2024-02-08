from django.core.management.base import BaseCommand
from random import randint, choice
from market.models import ClientsModel


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        names = ['Роберт', 'Алексей', 'Михаил', 'Максим', 'Иван', 'Григорий', 'Константин']
        surnames = ['Семенов ', 'Бочаров ', 'Болдырев ', 'Ларионов ', 'Капустин ', 'Тихомиров ', 'Ковалев ']
        adresses = ['Хуторская ул.', 'Интернациональная ул.', 'Мичурина ул.', 'Южная ул.']
        for i in range(0, 5):
            client = ClientsModel(name=f'{choice(surnames)}{choice(names)}',
                                  email=f'client{i}@mail.ru',
                                  phone=str(randint(1_000_000, 9_999_999)),
                                  address=f'{choice(adresses)}, д.{i}',
                                  )
            client.save()
            print(f'Создан Клиент: {client} ')
