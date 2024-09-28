from django.contrib import admin
from .models import Credit, Payment, ClientCreditProduct, InterestRate

admin.site.register(Credit)
admin.site.register(Payment)
admin.site.register(ClientCreditProduct)
admin.site.register(InterestRate)

# Register your models here.
