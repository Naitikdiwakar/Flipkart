from django.urls import path,include
from customer.views import *
urlpatterns = [
    path('get-customers',GetcustomerView.as_view()),  
     path('get-customers-address',GetcustomerAddressView.as_view()),   
]