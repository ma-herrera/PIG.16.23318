from django.urls import path
from .views import Registro, cerrar_sesion, loguear, ListadoUsuario, RegistrarUsuario

urlpatterns = [
    path ('', Registro.as_view(), name="usuario"),
    path ('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path ('loguear', loguear, name="loguear"),
    path ('listado_usuarios/', ListadoUsuario.as_view(), name='listar_usuarios'),
    path ('registrar_usuarios/',RegistrarUsuario.as_view(), name='registrar_usuarios')
]