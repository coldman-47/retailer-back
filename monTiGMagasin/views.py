from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, HttpResponse
from monTiGMagasin.config import baseUrl
from monTiGMagasin.models import InfoProduct
from monTiGMagasin.serializers import InfoProductSerializer

# Create your views here.
class InfoProductList(APIView):
    def get(self, request, format=None):
        products = InfoProduct.objects.all()
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)
    
class InfoProductDetail(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)

class PutProductOnSale(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, new_price, format=None):
            product = InfoProduct.objects.get(tig_id=tig_id)
            product.discount = float(new_price)
            product.sale = True
            product.save()
            serializer = InfoProductSerializer(product)
            return Response(serializer.data)

class RemoveOnSale(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, format=None):
            product = InfoProduct.objects.get(tig_id=tig_id)
            product.discount = 0
            product.sale = False
            product.save()
            serializer = InfoProductSerializer(product)
            return Response(serializer.data)

class IncrementStock(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, number, format=None):
            product = InfoProduct.objects.get(tig_id=tig_id)
            product.quantityInStock = product.quantityInStock + number
            product.save()
            serializer = InfoProductSerializer(product)
            return Response(serializer.data)

class DecrementStock(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, number, format=None):
            product = InfoProduct.objects.get(tig_id=tig_id)
            if product.quantityInStock >= number:
                product.quantityInStock = product.quantityInStock - number
                product.save()
            serializer = InfoProductSerializer(product)
            return Response(serializer.data)
        
class UpdateSales(APIView):
    def get(self, request, format=None):
        products = InfoProduct.objects.all()
        for product in products:
            if product.quantityInStock > 16 and product.sale == False:
                product.sale = True
                product.save()
            elif product.quantityInStock <= 16 and product.sale:
                product.sale = False
                product.save()
        return Response("ok")