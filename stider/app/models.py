from django.db import models

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    phone=models.IntegerField(default=0)
    password=models.CharField(max_length=30)
    
    
    def login_user(email,password):
        return Signup.objects.filter(email=email,password=password)
    
    

