from django.urls import path
from .views import index,formulario_terror,formulario_cienciaficcion,formulario_comedia,lista_terror

urlpatterns = [path('',index,name="index"),
               path('comedia/',formulario_comedia,name="pelis comedia"),
               path('ciencia-ficcion/',formulario_cienciaficcion, name = "ciencia ficion"),
               path('terror/agregar',formulario_terror,name="formulario terror"),
               path('lista_terror/', lista_terror, name='lista_de_terror')]
