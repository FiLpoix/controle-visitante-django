# Generated by Django 5.1.1 on 2024-10-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartamentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartamento',
            name='vagas_estacionamento',
            field=models.IntegerField(default=1, verbose_name='Quantidade de vagas no estacionamento'),
        ),
    ]
