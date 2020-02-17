from django.urls import path
from . import views

app_name='solicitacao'

urlpatterns = [
    path('assuntos/', views.AssuntosList.as_view()),
    path('solicitacoes/', views.Solicitacoes.as_view()),
#    path('solicitacao/', views.Solicitacao.as_view()),
#    path('telefones/<int:item>', views.TelefoneList.as_view()),
]