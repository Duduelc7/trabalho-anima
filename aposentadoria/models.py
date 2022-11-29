from django.db import models

# Create your models here.


class Trabalho(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)
    genero = models.CharField(max_length=255, blank=True, null=True)
    anos_trabalho = models.IntegerField(blank=True, null=True)
    tempo_aposentar = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trabalho'

    def __str__(self):

        return "{} - {}".format(self.nome,self.anos_trabalho)
