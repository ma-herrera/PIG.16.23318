from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home_administracion, name="home_administracion"),
    
    path('tipo_de_actividad/', views.TipoDeActividadIndexListView.as_view(), name="tipo_de_actividad_index_view"),
    path('tipo_de_actividad/nuevo/', views.TipoDeActividadNuevoView.as_view(), name="tipo_de_actividad_nuevo_view"),
    path('tipo_de_actividad/editar/<int:pk>', views.TipoDeActividadUpdateView.as_view(), name="tipo_de_actividad_editar_view"),
    path('tipo_de_actividad/eliminar/<int:pk>', views.TipoDeActividadDeleteView.as_view(), name="tipo_de_actividad_eliminar_view"),
    path('tipo_de_actividad/buscar/', views.tipo_de_actividad_buscar,name='tipo_de_actividad_buscar'),

    path('profesor/', views.ProfesorIndexListView.as_view(), name="profesor_index_view"),
    path('profesor/nuevo/', views.ProfesorNuevoView.as_view(), name="profesor_nuevo_view"),
    path('profesor/editar/<int:pk>', views.ProfesorUpdateView.as_view(), name="profesor_editar_view"),
    path('profesor/eliminar/<int:pk>', views.ProfesorDeleteView.as_view(), name="profesor_eliminar_view"),
    path('profesor/buscar/', views.profesor_buscar,name='profesor_buscar'),

    # path('tipo_de_actividad/', views.tipo_de_actividad_index,name='tipo_de_actividad_index'),
    # path('tipo_de_actividad/nuevo/', views.tipo_de_actividad_nuevo,name='tipo_de_actividad_nuevo'),
    # path('tipo_de_actividad/editar/<int:id_tipo_de_actividad>', views.tipo_de_actividad_editar,name='tipo_de_actividad_editar'),
    # path('tipo_de_actividad/eliminar/<int:id_tipo_de_actividad>', views.tipo_de_actividad_eliminar,name='tipo_de_actividad_eliminar'),
]