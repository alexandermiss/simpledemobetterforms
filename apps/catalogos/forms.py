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

    def save(self, commit=True):
        objects = super(EmpleadoPersonaModelForm, self).save(commit=False)

        if commit:
            persona = objects['persona']
            persona.save()
            empleado = objects['empleado']
            empleado.persona = persona
            empleado.save()

        return objects