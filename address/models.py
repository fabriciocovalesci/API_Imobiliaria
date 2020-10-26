from django.db import models


class AddresState(models.Model):
    state = models.CharField(max_length=2)


class AddressCity(models.Model):
    city = models.CharField(max_length=100)
    state = models.ForeignKey(AddresState, on_delete=models.CASCADE)



class AddressNeighborhood(models.Model):
    neighborhood = models.CharField(max_length=100)
    city = models.ForeignKey(AddressCity, on_delete=models.CASCADE)



class AddressStreet(models.Model):
    street = models.CharField(max_length=100)
    cep = models.CharField(max_length=12)
    neighborhood = models.ForeignKey(AddressNeighborhood, on_delete=models.CASCADE)



class Address(models.Model):
    state = models.CharField(max_length=2 , null=True, blank=True)
    city = models.CharField(max_length=100 , null=True, blank=True)
    neighborhood = models.CharField(max_length=100 , null=True, blank=True)
    street = models.CharField(max_length=100 , null=True, blank=True)
    number = models.CharField(max_length=8, null=True, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return self.street