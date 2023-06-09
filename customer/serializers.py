from rest_framework import serializers
from customer.models import *
class GetcustomerSerializer(serializers.ModelSerializer):


    class Meta:
        model =Customers
        fields = "__all__"


class GetcustomerAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAddress
        fields = "__all__"


class GetcustomerDetailsAddresserializer(serializers.ModelSerializer):
    customer_address = GetcustomerAddressSerializer(many=True)

    class Meta: 
        model=Customers
        fields=('first_name','last_name','mobile','age','country','dob','customer_address')