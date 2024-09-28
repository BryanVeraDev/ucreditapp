from django.db import models
from status.models import StatusGeneral

class Product(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    status = models.ForeignKey(StatusGeneral, on_delete=models.CASCADE)
    product_type = models.ForeignKey('ProductType', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.description