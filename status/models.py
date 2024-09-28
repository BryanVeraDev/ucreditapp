from django.db import models

class StatusGeneral(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.description
    
class StatusCredit(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20)
    
    def __str__(self):
        return self.description

class StatusPayment(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20)
    
    def __str__(self):
        return self.description      
