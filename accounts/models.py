from django.db import models
from cpf_field.models import CPFField
from django.contrib.auth.models import User
from address.models import AddressStreet

# my account 0x2FC2A6876f384378882700f3125621fDA6C88b2f

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = CPFField('cpf')
    account = models.CharField(max_length=100, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cellphone = models.CharField(max_length=12, null=True, blank=True)
    address = models.ForeignKey(AddressStreet, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'pessoa'
        verbose_name_plural = u'pessoas'


