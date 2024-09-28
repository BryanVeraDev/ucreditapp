from django.db import models
from status.models import StatusGeneral

class User(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    registration_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=50)
    status = models.ForeignKey(StatusGeneral, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Client(User):
    pass


class Employee(User):
    password = models.CharField(max_length=80)

class Administrator(User):
    password = models.CharField(max_length=80)
