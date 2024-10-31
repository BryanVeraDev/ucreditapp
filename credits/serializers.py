from rest_framework import serializers
from .models import Credit, Payment, InterestRate, ClientCreditProduct

from products.models import Product
from products.serializers import ProductInfoSerializer

from clients.models import Client
from clients.serializers import ClientInfoSerializer

class PaymentSerializer(serializers.ModelSerializer):
    credit = serializers.PrimaryKeyRelatedField(queryset=Credit.objects.all(), write_only=True)
    
    class Meta:
        model = Payment
        fields = [
            'id', 
            'payment_amount', 
            'payment_date', 
            'due_date', 
            'status', 
            'credit'
            ]
        
class InterestRateSerializer(serializers.ModelSerializer):   
    
    class Meta:
        model = InterestRate
        fields = '__all__'
        
class InterestRateInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InterestRate
        exclude = ['id']
        
class ClientCreditProductSerializer(serializers.ModelSerializer):
    id_product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
    product_info = ProductInfoSerializer(source='id_product', read_only=True)
    
    class Meta:
        model = ClientCreditProduct
        fields = [
            'id_product', 
            'product_info', 
            'quantity'
            ]
        
class CreditSerializer(serializers.ModelSerializer):
    products = ClientCreditProductSerializer(source='clientcreditproduct_set', many=True)
    
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), write_only=True)
    client_info = ClientInfoSerializer(source='client', read_only=True)
    
    interest_rate = serializers.PrimaryKeyRelatedField(queryset=InterestRate.objects.all(), write_only=True)
    interest_rate_info = InterestRateInfoSerializer(source='interest_rate', read_only=True)
    
    class Meta:
        model = Credit
        fields = [
            'id', 
            'description', 
            'total_amount', 
            'no_installment', 
            'application_date', 
            'start_date', 
            'end_date', 
            'penalty_rate', 
            'status', 
            'interest_rate', 
            'interest_rate_info',
            'client', 
            'client_info', 
            'products']
    
    
    def create(self, validated_data):
        products_data = validated_data.pop('clientcreditproduct_set')
        credit = Credit.objects.create(**validated_data)
        
        for product_data in products_data:
            ClientCreditProduct.objects.create(id_credit=credit, **product_data)
            
        return credit
    
    
    
    def update(self, instance, validated_data):
        product_data = validated_data.pop('clientcreditproduct_set', [])
        
        """"
        Extended form
        instance.description = validated_data.get('description', instance.description)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.no_installment = validated_data.get('no_installment', instance.no_installment)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.penalty_rate = validated_data.get('penalty_rate', instance.penalty_rate)
        instance.status = validated_data.get('status', instance.status)
        instance.interest_rate = validated_data.get('interest_rate', instance.interest_rate)
        instance.client = validated_data.get('client', instance.client)
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
       
        instance.save()
        
        new_product_ids = [product['id_product'].id for product in product_data]
        
        instance.clientcreditproduct_set.exclude(id_product__in=new_product_ids).delete()
        
        for product in product_data:
            ClientCreditProduct.objects.update_or_create(id_credit=instance, id_product=product['id_product'].id, defaults=product)
       
        return instance
        

    