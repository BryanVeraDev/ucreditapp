from django.contrib import admin
from .models import Credit, Payment, ClientCreditProduct, InterestRate

class ClientCreditProductInLine(admin.TabularInline):
    model = ClientCreditProduct
    extra = 1

class CreditAdmin(admin.ModelAdmin):
    inlines = [ClientCreditProductInLine]
    
admin.site.register(Credit, CreditAdmin)
admin.site.register(Payment)
admin.site.register(ClientCreditProduct)
admin.site.register(InterestRate)


