from django.urls import path
from . import views

app_name='bemprego'

urlpatterns = [
    path('escolaridades/', views.EscolaridadesList.as_view()),
    path('vagas/<int:escolaridade>', views.VagasList.as_view()),
]