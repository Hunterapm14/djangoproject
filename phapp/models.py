from django.db import models

# Create your models here.
class Customer(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Email=models.EmailField()
    Password=models.CharField(max_length=20)

class Images(models.Model):
    Photo=models.ImageField(upload_to='img/',null=True,blank=True)
    PhotoName=models.CharField(max_length=20)
    Creator=models.CharField(max_length=20)