from django.db import models

# Create your models here.

class Apartamento(models.Model):
    numero_apartamento = models.CharField(verbose_name='Numero do apartamento', max_length=5)
    bloco_apartamento = models.CharField(verbose_name='Bloco do apartamento', max_length=3)
    vagas_estacionamento = models.CharField(verbose_name='Quantidade de vagas no estacionamento', max_length=4)

    class Meta:
        verbose_name= 'Apartamento'
        verbose_name_plural= 'Apartamentos'
        db_table= 'apartamento'
    
    def __str__(self):
        return self.numero_apartamento
