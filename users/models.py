from django.db import models
from django.contrib.auth.models import User
from home.models import EmailList
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    name = models.CharField(max_length=100, null= True)
    company= models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    image = models.ImageField(upload_to='media', null=True)
    bio = models.TextField(null=True)
    
    def __str__(self):
        return self.user.username