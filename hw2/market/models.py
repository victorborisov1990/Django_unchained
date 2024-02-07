from django.db import models


class ClientsModel(models.Model):
	"""
	Поля модели «Клиент»:
	— имя клиента
	— электронная почта клиента
	— номер телефона клиента
	— адрес клиента
	— дата регистрации клиента
	"""
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=200)
	registration_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f'{self.name} {self.phone}'


class ProductsModel(models.Model):
	"""
	Поля модели «Товар»:
	— название товара
	— описание товара
	— цена товара
	— количество товара
	— дата добавления товара
	"""
	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.FloatField()
	quantity = models.IntegerField()
	added_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f'{self.name}: {self.quantity} шт по {self.price:.2f} руб.'


class OrdersModel(models.Model):
	"""
	Поля модели «Заказ»:
	— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
	— связь с моделью «Товар», указывает на товары, входящие в заказ
	— общая сумма заказа
	— дата оформления заказа
	"""
	client = models.ForeignKey(ClientsModel, on_delete=models.CASCADE)
	product = models.ManyToManyField(Product)
	amount = models.FloatField()
	ordered_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f'client: {self.client}, product: {self.product}'
