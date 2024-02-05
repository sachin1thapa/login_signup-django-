from typing import Any
from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length = 50)
    img = models.ImageField(upload_to='img')
    author = models.CharField(max_length = 20 , default = "Sachin")
    email = models.EmailField(blank = True)
    desc = models.TextField(default = "Available in List library" , max_length = 30)
    offer = models.BooleanField(default = False)


# database ma name ko thau ma default ma database object vanerwdekau cha ani yo use gare name wa id wa k vanerw dekaune chai specify garnw parcha 
                         
    def __str__(self):                           
        return self.name
    
