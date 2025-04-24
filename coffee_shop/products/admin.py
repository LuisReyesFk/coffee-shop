from django.contrib import admin

from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("id_product", "name", "price", "description", "image")
    search_fields = ("name", "description")

admin.site.register(Product, ProductAdmin)