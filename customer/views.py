from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.models import *
from customer.serializers import *
from rest_framework.response import Response


# Create your views here.

class GetcustomerView(APIView):

    def get(self,request):

        instance =Customers.objects.all()
        serializer =GetcustomerSerializer(instance,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        params=request.data
        print("data--",params)
        ser = GetcustomerSerializer(data=params)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({"msg":"Save successfully!!!!"}) 
    
class GetcustomerAddressView(APIView):

    def get(self,request):
        instance =CustomerAddress.objects.all()
        serializer =GetcustomerSerializer(instance,many=True)
        return Response(serializer.data)
    

class GetcustomerDeatailsAddressview(APIView):
    def get(self,request,pk):
        instances=Customers.objects.filter(id=pk)  
        ser= GetcustomerDetailsAddreserializer(instances,many=True)
        return Response(ser.data)