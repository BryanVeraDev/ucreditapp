from django.shortcuts import render

# Create your views here.

from .models import Credit, Payment, InterestRate, ClientCreditProduct
from .serializers import CreditSerializer, PaymentSerializer, InterestRateSerializer, ClientCreditProductSerializer

from django.core.serializers import serialize

from rest_framework import routers, serializers, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class ClientCreditProductViewSet(viewsets.ModelViewSet):
    queryset = ClientCreditProduct.objects.all()
    serializer_class = ClientCreditProductSerializer
    
class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class InterestRateViewSet(viewsets.ModelViewSet):
    queryset = InterestRate.objects.all()
    serializer_class = InterestRateSerializer
    
