from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status


from base.models import Product
from base.serializers import ProductSerializer

from rest_framework import status


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    print('$'*900)
    # product = get_object_or_404(Product, _id=pk)
    # product = Product.objects.get(_id=pk)
    try:
        product = Product.objects.get(_id=pk)
    except Product.DoesNotExist:
        return Response({'Details': 'Product Not Found!'}, status.HTTP_404_NOT_FOUND)
    print('='*200)
    print(product)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
