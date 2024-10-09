from django.db import models

# Create your models here.

class Morador(models.Model):
    nome_completo = models.CharField(verbose_name='Nome completo do morador', max_length=200)
    contato = models.CharField(verbose_name='Contato do morador ', max_length=11)
    apartamento = models.CharField(verbose_name='Apartamento do morador', max_length=10)

    class Meta:
        verbose_name = "Morador"
        verbose_name_plural = "Moradores"
        db_table = "morador"
    
    def __str__(self):
        return self.nome_completo