import json
from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from revendeurBackOffice.models import Product
from revendeurBackOffice.serializers import ProductSerializer

# Create your views here.
class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class UpdateProduct(APIView):
    # def get_object(self, pk):
    #     try:
    #         return Product.objects.filter(pk=str(pk)).exists()
    #     except:
    #         raise Http404
        
    def put(self, request, format=None):
        body = request.body.decode('utf-8', errors='ignore')
        jsonData = json.loads(body)
        if isinstance(jsonData, list) == False:
            product = Product.objects.get(pk=jsonData['id'])
            serializer = ProductSerializer(instance=product, data=jsonData)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        else:
            for item in jsonData:
                product = Product.objects.get(pk=item['id'])
                serializer = ProductSerializer(instance=product, data=item)
                if serializer.is_valid():
                    serializer.save()
            return Response(jsonData)