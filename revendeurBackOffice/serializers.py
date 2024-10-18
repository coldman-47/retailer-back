from rest_framework.serializers import ModelSerializer
from revendeurBackOffice.models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'tig_id', 'name', 'category', 'price', 'sale', 'sale_percentage', 'discount', 'comments', 'stock', 'unit_sold')