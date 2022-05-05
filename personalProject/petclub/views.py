from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del servicio
# Create your views here.


class PetAPIView(APIView):
    def patch(self, request):
        return Response(data="Estoy en el patch",status=200)
    def get(self, request):
        return Response(data="Estoy en el getd",status=200)
    def delete(self, request):
        return Response(data="Estoy en el delete",status=200)
    def post(self, request):
        return Response(data="Estoy en el post",status=200)

class PersonAPIView(APIView):
    def get(self, request):
        return Response(data="Estoy en el get",status=200)
    def patch(self, request):
        return Response(data="Estoy en el patch",status=200)
    def delete(self, request):
        return Response(data="Estoy en el delete",status=200)
    def post(self, request):
        return Response(data="Estoy en el post",status=200)
