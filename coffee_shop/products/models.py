from django.db import models

# Create your models here.
class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="nombre")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    description = models.TextField(max_length=500, verbose_name="descripción")
    image = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="imagen")

    def __str__(self):
        return self.name