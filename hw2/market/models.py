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
	price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
	quantity = models.PositiveSmallIntegerField(default=0)
	added_date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='products', null=True, blank=True)
	# default = 'no_image.png'

	def __str__(self):
		return f'{self.name}'


class OrdersModel(models.Model):
	"""
	Поля модели «Заказ»:
	— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
	— связь с моделью «Товар», указывает на товары, входящие в заказ
	— общая сумма заказа
	— дата оформления заказа
	"""
	client = models.ForeignKey(ClientsModel, on_delete=models.CASCADE)
	product = models.ManyToManyField(ProductsModel)
	amount = models.FloatField(default=0)
	ordered_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f'Заказ {self.pk}: client: {self.client}, ordered_date: {self.ordered_date}'


class ProductList(models.Model):
	product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
