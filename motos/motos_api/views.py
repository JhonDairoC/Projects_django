from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Moto
from .serializers import MotoSerializer

# Create your views here.

class MotoListApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the moto items for give request user
        '''

        motos = Moto.objects
        serializer = MotoSerializer(motos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Moto whit give moto data
        '''
        data={
            'trademark': request.data.get('trademark'),
            'model': request.data.get('model'),
            'reference': request.data.get('reference'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }
        serializer = MotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class MotoDetailApiView(APIView):
    def get_object(self, moto_id):
        try:
            return Moto.objects.get(id=moto_id)
        except Moto.DoesNotExist:
            return None
        
    def get(self, request, moto_id, *args, **kwargs):
        moto_instance = self.get_object(moto_id)
        if not moto_instance:
            return Response(
                {"res": "Objeto moto id no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
            
        serializer = MotoSerializer(moto_instance)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, moto_id, *args, **kwargs):
        moto_instance = self.get_object(moto_id)
        if not moto_instance:
            return Response(
                {"res": "Objeto moto id no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        data = {
            'trademark': request.data.get('trademark'),
            'model': request.data.get('model'),
            'reference' : request.data.get('reference'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }
        serializer = MotoSerializer(
                instance = moto_instance,
                data = data,
                partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, moto_id, *args, **kwargs):
        moto_instance = self.get_object(moto_id)
        if not moto_instance:
            return Response(
                {"res": "Objecto moto id no existe"},
                status = status.HTTP_400_BAD_REQUEST
            )
        moto_instance.delete()
        return Response(
            {"res": "Objeto Eliminado"},
            status = status .HTTP_200_OK
            )