from django.urls import path
from . import views

app_name='comum'

urlpatterns = [
    path('telefones/', views.CategoriaTelefoneList.as_view()),
    path('telefones/<int:item>', views.TelefoneList.as_view()),
]