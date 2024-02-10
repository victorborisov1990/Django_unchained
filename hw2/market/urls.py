from django.urls import path
from . import views

urlpatterns = [
    path('client/<int:client_id>/', views.get_clients_products, name='get_clients_products'),
    path('add_product_image/<int:product_id>/', views.add_product_image, name='add_product_image'),
    path('', views.show_products, name='show_products'),
    path('select_product/', views.select_product_image, name='select_product_image'),
]

