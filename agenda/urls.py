from django.urls import path
from . import views

app_name='agenda'

urlpatterns = [
    path('assuntos/', views.AssuntosList.as_view()),
    path('agendas/', views.AgendasList.as_view()),
]