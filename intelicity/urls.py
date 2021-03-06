"""intelicity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import login, sample_api
from . import views


admin.site.site_header = "Intelicity"
admin.site.site_title = "Intelicity"

"""
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', login),
    path('api/sampleapi', sample_api),
#    path('usuarios/', views.UsuarioList.as_view()),

#    path('cidades/', views.CidadeList.as_view()),
#    path('bairros/<int:pk>', views.BairroList.as_view()),

    path('estados/', views.EstadoList.as_view()),
    path('cidades/<int:id>', views.CidadeList.as_view()),
    path('bairros/<int:id>', views.BairroList.as_view()),
    # Defesa Civil
#    path('dcivil/', include('dcivil.urls')),
    path('dcivil/', include('dcivil.urls', namespace='dcivil')),
    path('agenda/', include('agenda.urls', namespace='agenda')),
    path('bemprego/', include('bemprego.urls', namespace='bemprego')),
    path('comum/', include('comum.urls', namespace='comum')),
    path('solicitacao/', include('solicitacao.urls', namespace='solicitacao')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
#    path('login/', obtain_jwt_token),
]
