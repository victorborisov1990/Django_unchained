from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import ClientsModel, ProductsModel, OrdersModel
from datetime import datetime
from .forms import ImageForm, ProductListForm

def get_clients_products(request, client_id):
    """
    Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
    — за последние 7 дней (неделю)
    — за последние 30 дней (месяц)
    — за последние 365 дней (год)
    Товары в списке не должны повторятся.
    """
    print(client_id)
    client = get_object_or_404(ClientsModel, pk=client_id)
    orders = OrdersModel.objects.filter(client=client_id)
    product_list_7 = []
    product_list_30 = []
    product_list_365 = []
    for order in orders:
        delta = datetime.now().date() - order.ordered_date.date()
        for product in order.product.all():
            if delta.days <= 7:
                product_list_7.append(product)
            if delta.days <= 30:
                product_list_30.append(product)
            if delta.days <= 365:
                product_list_365.append(product)
    product_list_7 = set(product_list_7)
    product_list_30 = set(product_list_30)
    product_list_365 = set(product_list_365)
    context = {"client": client,
               "product_list_7": product_list_7,
               "product_list_30": product_list_30,
               "product_list_365": product_list_365}
    return render(request, 'market/clients_products.html', context)


def add_product_image(request, product_id):
    product = get_object_or_404(ProductsModel, pk=product_id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get("image")
            product.image = img
            product.save()
            return redirect('select_product_image')
    else:
        form = ImageForm()
    context = {'form': form, 'title': product.name}
    return render(request, 'market/products_image.html', context)


def select_product_image(request):
    if request.method == 'POST':
        form = ProductListForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data.get("product")
            pk = product.pk
            # return HttpResponse(f'id: {pk}, название: {name}, цена: {price} руб.')
            return redirect('add_product_image', product_id=pk)
    else:
        form = ProductListForm()
    context = {'form': form, 'title': 'Выбор продукта'}
    return render(request, 'market/select_product.html', context)


def show_products(request):
    products = ProductsModel.objects.all()
    context = {'products': products, 'title': 'Продукты'}
    return render(request, 'market/all_products.html', context)
