from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)


class Empleado(models.Model):
    CATEGORIAS = (
        ('0', 'Secretario'),
        ('1', 'Tesorero'),
        ('2', 'Jefe')
    )
    categoria = models.CharField(choices=CATEGORIAS, max_length=2)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='individuos', related_query_name='individuo')