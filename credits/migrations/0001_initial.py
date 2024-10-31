# Generated by Django 5.1.1 on 2024-10-31 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestRate',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='ClientCreditProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField()),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('no_installment', models.SmallIntegerField()),
                ('application_date', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('penalty_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('paid', 'Paid'), ('default', 'Default')], max_length=15)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='clients.client')),
                ('products', models.ManyToManyField(through='credits.ClientCreditProduct', to='products.product')),
                ('interest_rate', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='credits.interestrate')),
            ],
        ),
        migrations.AddField(
            model_name='clientcreditproduct',
            name='id_credit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='credits.credit'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('payment_date', models.DateField()),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], max_length=15)),
                ('credit', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='credits.credit')),
            ],
        ),
        migrations.AddConstraint(
            model_name='clientcreditproduct',
            constraint=models.UniqueConstraint(fields=('id_credit', 'id_product'), name='unique_client_credit_product'),
        ),
    ]
