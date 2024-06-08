from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)  #Camapos obligatorios por no indicar si pueden quedar en blanco
    last_name = models.CharField(max_length=50)   
    email = models.EmailField(max_length=50, blank=True, null=True)  #Campos opcioneles
    age = models.PositiveIntegerField(blank=True, null=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
