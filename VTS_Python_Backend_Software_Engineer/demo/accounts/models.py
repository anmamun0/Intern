 # myapp/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Product model
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        permissions = [
            ("can_publish", "Can publish product"),
            ("can_discount", "Can give discount on product"),
        ]
        
    def __str__(self):
        return self.name


# Order model (for extra practice)
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # ordered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"
