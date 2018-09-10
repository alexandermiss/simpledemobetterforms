from django.urls import path
from .views import EmpleadoCreateView, SuccessView


urlpatterns = [
    path('', EmpleadoCreateView.as_view(), name='index'),
    path('success/', SuccessView.as_view(), name='success'),
]