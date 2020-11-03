from django.db import models
from address.models import AddressStreet
class TypeImmobile(models.Model):
    typeIm = models.CharField(max_length=150,  null=True, blank=True)


class Immobile(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    condominium = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    typeIm = models.ForeignKey(TypeImmobile, related_name='immobile', on_delete=models.CASCADE,  null=True, blank=True)
    photo = models.ImageField(upload_to='photoImmobile')
    address = models.ForeignKey(AddressStreet, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
