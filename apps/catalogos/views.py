from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, UpdateView

from .forms import EmpleadoPersonaModelForm
from .models import Persona, Empleado


class EmpleadoCreateView(CreateView):
    form_class = EmpleadoPersonaModelForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('success')


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoPersonaModelForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('success')

    def get_form_kwargs(self):
        kwargs = super(EmpleadoUpdateView, self).get_form_kwargs()
        
        kwargs.update(instance={
            'domicilio': self.object.persona.domicilio,
            'persona': self.object.persona,
            'empleado': self.object
        })
        return kwargs


class SuccessView(TemplateView):
    template_name = 'success.html'
