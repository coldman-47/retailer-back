import time
from django.core.management.base import BaseCommand
import requests

from revendeurBackOffice.models import Product
from revendeurBackOffice.serializers import ProductSerializer
from revendeurBackOffice.config import baseUrl

class Command(BaseCommand):
    help = 'Refresh the list of products from TiG server.'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        for product in jsondata:
            if Product.objects.filter(tig_id=product['id']).exists() == False:
                serializer = ProductSerializer(data={
                                                        'tig_id':str(product['id']),
                                                        'name':str(product['name']),
                                                        'category':str(product['category']),
                                                        'price':str(product['price']),
                                                        'unit':str(product['unit']),
                                                        'availability':str(product['availability']),
                                                        'sale':str(product['sale']),
                                                        'discount':str(product['discount']),
                                                        'comments':str(product['comments']),
                                                        'owner':str(product['owner'])
                                                        })
                if serializer.is_valid():
                    serializer.save()
                    self.stdout.write(self.style.SUCCESS('['+time.ctime()+'] Successfully added product id="%s"' % product['id']))
        self.stdout.write('['+time.ctime()+'] Data refresh terminated.')
