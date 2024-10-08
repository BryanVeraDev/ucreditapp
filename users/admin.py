from django.contrib import admin
from .models import Client, Employee, Administrator

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    exclude = ('groups', 'user_permissions')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    exclude = ('groups', 'user_permissions')

@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    exclude = ('groups', 'user_permissions')
