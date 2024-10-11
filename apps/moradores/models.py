from django.db import models

from apartamentos.models import Apartamento


# Create your models here.

class Morador(models.Model):
    nome_completo = models.CharField(verbose_name='Nome completo do morador', max_length=200)
    contato = models.CharField(verbose_name='Contato do morador ', max_length=11)
    apartamento = models.ForeignKey(Apartamento, verbose_name='Apartamento', on_delete=models.PROTECT)
    cpf = models.CharField(verbose_name='CPF', max_length=11)

    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)
            
            cpf_parte_um = cpf[0:3]
            cpf_parte_dois = cpf[3:6]
            cpf_parte_tres = cpf[6:9]
            cpf_parte_quatro = cpf[9:]
            
            cpf_formatado = f'{cpf_parte_um}.{cpf_parte_dois}.{cpf_parte_tres}-{cpf_parte_quatro}'
            return cpf_formatado

    class Meta:
        verbose_name = "Morador"
        verbose_name_plural = "Moradores"
        db_table = "morador"
    
    def __str__(self):
        return self.nome_completo