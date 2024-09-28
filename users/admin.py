from django.contrib import admin
from .models import User, Client, Employee, Administrator, StatusGeneral

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Administrator)

