from django import forms
from django.forms import ModelForm
from .models import ProductList


class ImageForm(forms.Form):
    image = forms.ImageField()


class ProductListForm(ModelForm):
    class Meta:
        model = ProductList
        fields = ['product']
