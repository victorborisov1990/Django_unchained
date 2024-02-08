from django.urls import path, include
from . import views

urlpatterns = [
    path('client/<client_id>/', views.get_clients_products, name='get_clients_products'),

]
