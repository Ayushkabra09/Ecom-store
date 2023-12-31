from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializer import ProducSerializer
from .products import products

# Create your views here.

@api_view(["GET"])

def getRoutes(request):

    routes = [

    ]

    return Response(routes)
@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProducSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serialzer = ProducSerializer(product, many=False)
    return Response(serialzer.data) 

