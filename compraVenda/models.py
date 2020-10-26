from django.db import models
from cpf_field.models import CPFField

# my account 0x2FC2A6876f384378882700f3125621fDA6C88b2f

class Usuario(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    cpf = CPFField('cpf')
    account = models.CharField(max_length=100)
    telefone = models.CharField(max_length=12)
    endereco = models.CharField(max_length=250)

    class Meta:
        ordering = ['first_name']
        verbose_name = u'pessoa'
        verbose_name_plural = u'pessoas'

    def __str__(self):
        return self.first_name + " " + self.last_name

    full_name = property(__str__)


class CadastroImovel(models.Model):
    tipoImovel = models.CharField(max_length=200)
    condominio = models.DecimalField(max_digits=6, decimal_places=2)
    valorImovel = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    localizacao = models.TextField()
    fotos = models.ImageField(upload_to='cadastroImovel', null=True, blank=True)