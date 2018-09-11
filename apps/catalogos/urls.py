from django.urls import path, re_path
from .views import EmpleadoCreateView, SuccessView, EmpleadoUpdateView


urlpatterns = [
    path('', EmpleadoCreateView.as_view(), name='index'),
    path('actualizar/<int:pk>/', EmpleadoUpdateView.as_view(), name='actualizar'),
    path('success/', SuccessView.as_view(), name='success'),
]