from django.urls import path
from .views import home, contactos, nosotros, servicios

urlpatterns = [
    path('', home, name='home'),
    path('contactos', contactos, name='contactos'),
    path('nosotros', nosotros, name='nosotros'),
    path('servicios',servicios, name='servicios'),
]
