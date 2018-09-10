from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView

from .forms import EmpleadoPersonaModelForm


class EmpleadoCreateView(CreateView):
    form_class = EmpleadoPersonaModelForm
    template_name = 'formulario.html'

    def form_valid(self, form):
        persona = form['persona'].save()
        empleado = form['empleado'].save(commit=False)
        empleado.persona = persona
        empleado.save()
        return HttpResponseRedirect(reverse('success'))


class SuccessView(TemplateView):
    template_name = 'success.html'
