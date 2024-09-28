from django.db import models
from status.models import StatusCredit, StatusPayment
from users.models import Client
from products.models import Product

class Credit(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=11, decimal_places=2)
    no_installment = models.SmallIntegerField()
    application_date = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    penalty_rate = models.DecimalField(max_digits=4, decimal_places=2)
    interest_rate = models.ForeignKey('InterestRate', on_delete=models.CASCADE)    
    status = models.ForeignKey(StatusCredit, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.description

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    payment_amount = models.DecimalField(max_digits=11, decimal_places=2)
    payment_date = models.DateField()
    due_date = models.DateField()
    status = models.ForeignKey(StatusPayment, on_delete=models.CASCADE)
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.credit.description}'

class ClientCreditProduct(models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_credit = models.ForeignKey(Credit, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_client',  'id_product', 'id_credit'], name='unique_client_credit_product')
        ]
        
    def __str__(self) -> str:
        return f'{self.id_client.name} - {self.id_credit}'
    
class InterestRate(models.Model):
    id = models.SmallAutoField(primary_key=True)
    percentage = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __str__(self) -> str:
        return f'{self.percentage}'
    
    
    