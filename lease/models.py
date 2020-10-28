from django.db import models
from django.utils import timezone


from accounts.models import Profile
from immobile.models import Immobile


def pay_day():
    return timezone.now() + timezone.timedelta(days=30)

class Lease(models.Model):

    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    client = models.ForeignKey(Profile, related_name='Leaseclient', on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, related_name='Leasesalesman', on_delete=models.CASCADE)
    immobile = models.ForeignKey(Immobile, on_delete=models.CASCADE)
    multa = models.IntegerField(default=0.10)
    payday = models.DateField(default=pay_day())
