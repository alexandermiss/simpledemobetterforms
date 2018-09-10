from django.forms import ModelForm

from betterforms.multiform import MultiModelForm

from .models import Persona, Empleado


class PersonaModelForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'


class EmpleadoModelForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['categoria', 'salario']


class EmpleadoPersonaModelForm(MultiModelForm):
    form_classes = {
        'persona': PersonaModelForm,
        'empleado': EmpleadoModelForm,
    }
