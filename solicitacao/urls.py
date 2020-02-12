from django.urls import path
from . import views

app_name='solicitacao'

urlpatterns = [
    path('solicitacoes/', views.SolicitacoesList.as_view()),
#    path('telefones/<int:item>', views.TelefoneList.as_view()),
]