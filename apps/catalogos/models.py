from django.db import models


class Domicilio(models.Model):
    calle = models.CharField(max_length=150)
    colonia = models.CharField(max_length=100)


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE, related_name='domicilios',
                                  related_query_name='domicilio', null=True)


class Empleado(models.Model):
    CATEGORIAS = (
        ('0', 'Secretario'),
        ('1', 'Tesorero'),
        ('2', 'Jefe')
    )
    categoria = models.CharField(choices=CATEGORIAS, max_length=2)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='individuos',
                                related_query_name='individuo', null=True)
