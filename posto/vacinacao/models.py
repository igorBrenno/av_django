from django.db import models

# Create your models here.

class Criancas(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)
    nomeMae = models.CharField(max_length=200)
    vacina = models.CharField(max_length=200, blank=True)
    bairro = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.nome + " " + self.nomeMae + " " + self.vacina