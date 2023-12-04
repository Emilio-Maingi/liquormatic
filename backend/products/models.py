from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):

    name = models.CharField(max_length=256)
    description = models.TextField(max_length=512)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    stock = models.IntegerField()
    buying_price = models.IntegerField()
    selling_price = models.IntegerField()
    featured = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
