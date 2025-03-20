from django.contrib import admin
from django.urls import path
from .views import home, contacto, servicios, quienes_somos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('servicios/', servicios, name='servicios'),
    path('quienes-somos/', quienes_somos, name='quienes_somos'),
    path('contacto/', contacto, name='contacto'),
]
