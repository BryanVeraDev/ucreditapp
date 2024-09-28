from django.contrib import admin
from .models import StatusGeneral, StatusCredit, StatusPayment

admin.site.register(StatusGeneral)
admin.site.register(StatusCredit)
admin.site.register(StatusPayment)
