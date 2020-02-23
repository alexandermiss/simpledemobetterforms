from collections import OrderedDict
from django.forms import ModelForm

from betterforms.multiform import MultiModelForm

from .models import Persona, Empleado, Domicilio


class DomicilioModelForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = ['calle', 'colonia']


class PersonaModelForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido']


class EmpleadoModelForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['categoria', 'salario']


class EmpleadoPersonaModelForm(MultiModelForm):
    form_classes = OrderedDict({
        'persona': PersonaModelForm,
        'domicilio': DomicilioModelForm,
        'empleado': EmpleadoModelForm,
    })

    def save(self, commit=True):
        objects = super(EmpleadoPersonaModelForm, self).save(commit=False)

        if commit:
            domicilio = objects['domicilio']
            domicilio.save()
            persona = objects['persona']
            persona.domicilio = domicilio
            persona.save()
            empleado = objects['empleado']
            empleado.persona = persona
            empleado.save()

        return objects
