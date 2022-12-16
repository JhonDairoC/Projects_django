from tkinter import Entry
from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Produc
from .serializers import ProducSerializer

# Create your views here.
class ProducListApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the moto items for give request user
        '''
        produc = Produc.objects
        serializer = ProducSerializer(produc, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Moto whit give moto data
        '''
        data={
            'clasific': request.data.get('clasific'),
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }
        serializer = ProducSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ProducDetailApiView(APIView):
    def get_object(self, produc_id):
        try:
            return Produc.objects.get(id = produc_id)
        except Produc.DoesNotExist:
            return None
        
    def get(self, request, produc_id,*args, **kwargs):
        produc_instance = self.get_object(produc_id)
        if not produc_instance:
            return Response(
                {"res": "Objeto moto id no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
            
        serializer = ProducSerializer(produc_instance)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, produc_id, *args, **kwargs):
        produc_instance = self.get_object(produc_id)
        if not produc_instance:
            return Response(
                {"res": "Objeto no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        data={
            'clasific': request.data.get('clasific'),
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }
        serializer = ProducSerializer(
                instance = produc_instance,
                data = data,
                partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, produc_id, *args, **kwargs):
        produc_instance = self.get_object(id= produc_id)
        if not produc_instance:
            return Response(
                {"res": "Objecto moto id no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        produc_instance.delete()
        return Response(
            {"res": "Objeto Eliminado"},
            status = status .HTTP_200_OK
            )

            
#busqueda por clasificacion
class ClasificApiView(APIView):
    def get(self, request, produc_clasific,*args, **kwargs,):
        produc = Produc.objects.filter(clasific=produc_clasific)
        serializer = ProducSerializer(produc, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Moto whit give moto data
        '''
        data={
            'clasific': request.data.get('clasific'),
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }
        serializer = ProducSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class IdClasificApiView(APIView):
    def get_object(self , produc_clasific , id_clasific):
        try:
            return Produc.objects.get(clasific = produc_clasific , id = id_clasific)
        except Produc.DoesNotExist:
            return None
        
    def get(self, request, id_clasific, produc_clasific,*args, **kwargs):
        produc_instance = self.get_object(produc_clasific , id_clasific)
        if not produc_instance:
            return Response(
                {"res": "Objeto moto id no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
            
        serializer = ProducSerializer(produc_instance)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, produc_clasific , id_clasific, *args, **kwargs):
        produc_instance = self.get_object(produc_clasific , id_clasific)
        if not produc_instance:
            return Response(
                {"res": "Objeto no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        data={
            'clasific': request.data.get('clasific'),
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }
        serializer = ProducSerializer(
                instance = produc_instance,
                data = data,
                partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, produc_clasific , id_clasific, *args, **kwargs):
        produc_instance = self.get_object(produc_clasific , id_clasific)
        if not produc_instance:
            return Response(
                {"res": "Producto no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        produc_instance.delete()
        return Response(
            {"res": "Objeto Eliminado"},
            status = status .HTTP_200_OK
            )
