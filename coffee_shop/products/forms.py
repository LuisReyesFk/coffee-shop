from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nombre")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    description = forms.CharField(widget=forms.Textarea, max_length=500, label="Descripción")
    image = forms.ImageField(required=False, label="Imagen")

    def save_product(self):
        Product.objects.create(
            name=self.cleaned_data['name'],
            price=self.cleaned_data['price'],
            description=self.cleaned_data['description'],
            image=self.cleaned_data['image']
        )
# class Products(forms.Form):
#     products = forms.ModelChoiceField(queryset=Product.objects.all(), label="Productos")
    # Add any other fields you need for the list view
    # def save_product(self):