from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name= models.CharField(max_length=15,null=True,blank=True)
    last_name= models.CharField(max_length=15,null=True,blank=True)
    mobile= models.IntegerField(null=True,blank=True)
    addres= models.TextField(null=True,blank=True)
    age= models.IntegerField(null=True,blank=True)
    country= models.CharField(max_length=15,null=True,blank=True)
    city= models.CharField(max_length=20,null=True,blank=True)
    dob= models.DateField(max_length=15,null=True,blank=True)
    def __str__(self):
        return str(self.first_name)
    
class CustomerAddress(models.Model):
       customer=models.ForeignKey(Customers,on_delete=models.CASCADE,null=True,related_name="customer_address")
       street_name=models.CharField(max_length=15,null=True,blank=True)
       street_number=models.IntegerField(null=True,blank=True)
       country= models.CharField(max_length=15,null=True,blank=True)
       city= models.CharField(max_length=20,null=True,blank=True)
       state=models.CharField(max_length=15,null=True,blank=True)
       pincode=models.CharField(max_length=15,null=True,blank=True)
       def __str__(self):
        return str(self.street_name)

class CustomerAddhar(models.Model):
    customer=models.OneToOneField(Customers,on_delete=models.CASCADE)
    addher_no=models.IntegerField(null=True,blank=True)
    addher_name=models.CharField(max_length=12,null=True,blank=True)
    def __str__(self):
        return str(self.addher_name)


  
