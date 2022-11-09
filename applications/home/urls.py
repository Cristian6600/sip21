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
        'telefinia-ip', 
        views.TelefoniaTemplateView.as_view(),
        name='telefinia-ip',
    ),
    
    path(
        'infraestructura-telecomunicaciones', 
        views.InfraestructuraTemplateView.as_view(),
        name='infraestructura-telecomunicaciones',
    ),
    
    path(
        'seguridad-redes', 
        views.SeguridadTemplateView.as_view(),
        name='seguridad-redes',
    ),
    
    path(
        'cctv', 
        views.cctvTemplateView.as_view(),
        name='cctv',
    ),

    path(
        'obras-civiles', 
        views.ObrasCivilesTemplateView.as_view(),
        name='obras-civiles',
    ),
    
    path(
        'nosotros', 
        views.NosotrosTemplateView.as_view(),
        name='nosotros',
    ),
]