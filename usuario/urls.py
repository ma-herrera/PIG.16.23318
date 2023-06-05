from django.urls import path
from .views import  cerrar_sesion,  ListadoUsuario, RegistrarUsuario, EliminarUsuario, loguear, logoutUsuario

urlpatterns = [
   # path ('', Registro.as_view(), name="usuario"),
   #  path ('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path ('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion"),
    path ('loguear', loguear, name="loguear"),
    path ('listado_usuarios/', ListadoUsuario.as_view(), name='listar_usuarios'),
    path ('registrar_usuarios/', RegistrarUsuario.as_view(), name='registrar_usuarios'),
   # path ('eliminar/',EliminarUsuario.as_view(),name='eliminar_usuario'),

    

]