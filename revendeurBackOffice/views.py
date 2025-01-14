import json
from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from revendeurBackOffice.models import Operation, Product
from revendeurBackOffice.serializers import OperationSerializer, ProductSerializer, UserSerializer

# Create your views here.
class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
class ProductDetails(APIView):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        print(product)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
class UpdateProduct(APIView):
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
        
class OperationList(APIView):
    def get(self, request, format=None):
        operations = Operation.objects.prefetch_related('product').all()
        for op in operations:
            print(op.created_at)
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data)
    
class AddOperation(APIView):
    def post(self, request, format=None):
        body = request.body.decode('utf-8', errors='ignore')
        jsonData = json.loads(body)
        serializer = OperationSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save(product=Product.objects.get(id=jsonData['product']['id']))
        return Response(str(serializer.data))
    
class UpdateOperation(APIView):
    def put(self, request, pk):
        operation = Operation.objects.get(id=pk)
        body = request.body.decode('utf-8', errors='ignore')
        jsonData = json.loads(body)
        operation.created_at = jsonData['created_at']
        print(jsonData)
        serializer = OperationSerializer(instance = operation, data=jsonData)
        if serializer.is_valid():
            serializer.save()
        return Response(str(serializer.data))
    
class Registration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)