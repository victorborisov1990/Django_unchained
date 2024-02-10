from django.contrib import admin

from .models import ClientsModel, ProductsModel, OrdersModel

class ClientAdmin(admin.ModelAdmin):
    """Список Клиентов"""
    list_display = ['name', 'email', 'registration_date']
    ordering = ['registration_date']
    list_filter = ['address']
    search_fields = ['phone']
    search_help_text = 'Поиск по номеру телефона'

    """Отдельный Клиент"""
    fields = ['name', 'email', 'phone', 'address', 'registration_date']
    readonly_fields = ['registration_date']

admin.site.register(ClientsModel, ClientAdmin)

@admin.register(ProductsModel) # другой способ регистрации
class ProductAdmin(admin.ModelAdmin):
    """Список Продуктов"""
    list_display = ['name', 'price', 'quantity']
    ordering = ['price', '-quantity']
    search_fields = ['description']
    search_help_text = 'Поиск по описанию'

    """Отдельный продукт"""
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'image']
            }
        ),
        (
            'Описание',
            {
                'classes': ['collapse'],
                'fields': ['description']
            }
        ),
        (
            'Подробности',
            {
                'fields': ['price', 'quantity']
            }
        )
    ]


@admin.register(OrdersModel) # другой способ регистрации
class OrderAdmin(admin.ModelAdmin):
    """Список Заказов"""
    list_display = ['client', 'amount', 'ordered_date']
    ordering = ['amount', 'ordered_date']

    """Отдельный Заказ"""
    fields = ['client', 'product', 'amount', 'ordered_date']
    readonly_fields = ['ordered_date', 'amount']
