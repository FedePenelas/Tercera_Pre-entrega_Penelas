from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.avatar}"
    
class Avatar(models.Model):
    #Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Subcarpeta avatares de media
    avatar = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.avatar}"