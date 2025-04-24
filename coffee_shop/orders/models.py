from django.db import models
from django.contrib.auth.models import User
from products.models import Product  # Assuming you have a Product model in products app

# Create your models here.
class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    status = models.CharField(max_length=20, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50)
    tracking_number = models.CharField(max_length=50, blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Add any other fields you need for your order model
    def __str__(self):
        return f"Order {self.id_order} by {self.user.username}"
    
class OrderProduct(models.Model):
    id_order_product = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order {self.order.id_order}"