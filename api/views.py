from django.shortcuts import render
from rest_framework.decorators import api_view #DIZENDO QUE SÓ ACEITA O GET E POST 
from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework import status
from rest_framework.response import Response 

@api_view(['GET','POST'])
def listar_produtos(request):
    if request.method == 'GET':
        queryset = Produto.objects.all()   
        serializer = ProdutoSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProdutoSerializer(data = request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTPS_201_CREATED)
    else: 
        return Response(serializer.data, status=status.HTTP_480_BAD_REQUEST)     
            