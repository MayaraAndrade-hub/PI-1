from django.db import models

from django.db import models  
class Equipamento(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)   
    edataC = models.DateField()
    estatus = models.CharField(max_length=20)
    efornecedor = models.CharField(max_length=100)
    earea = models.CharField(max_length=50)
    eqtd = models.PositiveIntegerField()
    class Meta:  
        db_table = "equipamento"
