from rest_framework import serializers
from models import Product, Category

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length = 256)
    description = serializers.TextField(max_length = 512)
    # category = 
    stock = id = serializers.IntegerField()
    buying_price = serializers.IntegerField()
    selling_price = serializers.IntegerField()
    featured = serializers.BooleanField(required=False)