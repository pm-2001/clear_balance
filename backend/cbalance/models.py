from django.db import models

# Create your models here.
class Account(models.Model):
    account_number = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    # customer = models.ForeignKey('customer', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.account_number}'