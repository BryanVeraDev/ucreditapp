from django.db import models

class Product(models.Model):
    
    PRODUCT_STATUS = {
        "active":"Active",
        "inactive":"Inactive"    
    }
    
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    status = models.CharField(max_length=10, choices=PRODUCT_STATUS)
    product_type = models.ForeignKey('ProductType', on_delete=models.RESTRICT)
    
    def __str__(self) -> str:
        return self.name

class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.description