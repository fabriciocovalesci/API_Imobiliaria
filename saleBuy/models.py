from django.db import models
from accounts.models import Profile
from immobile.models import Immobile

class SaleBuy(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateTimeField()
    client = models.ForeignKey(Profile, related_name='SaleBuyclient', on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, related_name='SaleBuysalesman', on_delete=models.CASCADE)
    immobile = models.ForeignKey(Immobile, on_delete=models.CASCADE)

