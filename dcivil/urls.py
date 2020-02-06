from django.urls import path
from . import views

app_name='dcivil'

urlpatterns = [
    path('situacao/', views.SituacaoList.as_view()),
    path('situacoes/', views.SituacoesList.as_view()),
    path('responsaveis/', views.ResponsavelList.as_view()),
    path('pontosapoio/', views.PontosApoioList.as_view()),
    path('pontosapoio/<int:id>', views.PontosApoioList.as_view()),

#    path('responsaveis/', views.responsaveis),
#    path('responsaveis/', views.responsaveis, name='responsaveis'),
#    path('situacao/', views.situacao, name='situacao'),
]