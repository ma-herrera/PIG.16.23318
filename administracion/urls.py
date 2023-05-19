from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home_administracion, name="home_administracion"),
    path('tipo_de_actividad/', views.tipo_de_actividad_index,name='tipo_de_actividad_index'),
    path('tipo_de_actividad/nuevo/', views.tipo_de_actividad_nuevo,name='tipo_de_actividad_nuevo'),
    path('tipo_de_actividad/editar/<int:id_tipo_de_actividad>', views.tipo_de_actividad_editar,name='tipo_de_actividad_editar'),
    path('tipo_de_actividad/eliminar/<int:id_tipo_de_actividad>', views.tipo_de_actividad_eliminar,name='tipo_de_actividad_eliminar'),
]