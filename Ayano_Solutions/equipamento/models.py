from django.db import models

# Create your models here.

from django.db import models  
class Equipamento(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    emanutencao = models.CharField(max_length=3)  
    edataC = models.DateField() 
    class Meta:  
        db_table = "equipamento"