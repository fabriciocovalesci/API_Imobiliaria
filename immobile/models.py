from django.db import models

class TypeImmobile(models.Model):
    typeIm = models.CharField(max_length=150, null=False, blank=False)


class Immobile(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    condominium = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    typeIm = models.ForeignKey(TypeImmobile, related_name='immobile', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='./photoImmobile/immobile')

    def __str__(self):
        return self.title
