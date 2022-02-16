from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from django.shortcuts import get_object_or_404

from products import serializers


# Create your views here.
# , 'PUT', 'DELETE'serializer = ProductSerializer(serializer.data)
@api_view(['GET', 'POST'])
def product_list(request):

    products = Product.objects.all()


    if request.method == 'GET':

        serializer = ProductSerializer(products, many=True)
        
        return Response(serializer.data)

    elif request.method == 'POST':
    
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    

    # return Response(serializer.data)