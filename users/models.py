from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_STATUS = {
        "active":"Active",
        "inactive":"Inactive"
    }

    password = None
    last_login = None
    is_superuser = None
    username = None  
    is_staff = None
    is_active = None
    date_joined = None

    USERNAME_FIELD = 'id'
    
    id = models.CharField(max_length=12, primary_key=True)

    first_name = models.CharField(max_length=30, default='', blank=False)
    last_name = models.CharField(max_length=30, default='', blank=False)
    email = models.EmailField(unique=True, default='', blank=False)
    
    phone = models.CharField(max_length=12, default='', blank=False)
    registration_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=50, default='', blank=False)
    status = models.CharField(max_length=10, choices=USER_STATUS, default='', blank=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Evita el conflicto con 'auth.User'
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Evita el conflicto con 'auth.User'
        blank=True
    )
    
class Client(User):
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

class Employee(User):   
    password = models.CharField(max_length=80, default='', blank=False)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

class Administrator(User):
    password = models.CharField(max_length=80, default='', blank=False)

    class Meta:
        verbose_name = "Administrator"
        verbose_name_plural = "Administrators"