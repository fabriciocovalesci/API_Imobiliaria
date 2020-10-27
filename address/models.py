from django.db import models


class AddresState(models.Model):
    state = models.CharField(max_length=2)

class AddressCity(models.Model):
    city = models.CharField(max_length=100)

class AddressNeighborhood(models.Model):
    neighborhood = models.CharField(max_length=100)

class AddressStreet(models.Model):
    state = models.ForeignKey(AddresState, on_delete=models.CASCADE)
    city = models.ForeignKey(AddressCity,  on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(AddressNeighborhood,  on_delete=models.CASCADE)
    street = models.CharField(max_length=150, null=False, blank=True)
    number = models.CharField(max_length=8, null=False, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=False)

    def __str__(self):
        return self.street