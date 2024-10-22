from django.db import models

# Create your models here.
class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tig_id = models.IntegerField(default=-1)
    name = models.CharField(max_length=100, blank=True, default='')
    category = models.IntegerField(default=-1)
    price = models.FloatField(default=0)
    unit = models.CharField(max_length=20, blank=True, default='')
    availability = models.BooleanField(default=True)
    sale = models.BooleanField(default=False)
    sale_percentage = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    comments = models.CharField(max_length=100, blank=True, default='')
    owner = models.CharField(max_length=20, blank=True, default='tig_orig')
    stock = models.IntegerField(default=0)
    unit_sold = models.IntegerField(default=0)
    
class Operation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)