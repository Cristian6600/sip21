from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [

    path(
        '', 
        views.QHola.as_view(),
        name='publico',
    ),
    
    path(
        'contacto', 
        views.ContatoCreateView.as_view(),
        name='contacto',
    ),

    path(
        'software-medida', 
        views.SoftwareTemplateView.as_view(),
        name='software-medida',
    ),
    
    path(
        'analitica-big-data', 
        views.BigdataTemplateView.as_view(),
        name='analitica-big-data',
    ),
    
    path(
        'telefinia-ip', 
        views.TelefoniaTemplateView.as_view(),
        name='telefinia-ip',
    ),
    
    path(
        'infraestructura-telecomunicaciones', 
        views.InfraestructuraTemplateView.as_view(),
        name='infraestructura-telecomunicaciones',
    ),

]