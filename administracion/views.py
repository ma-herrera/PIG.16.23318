from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from administracion.forms import TipoDeActividadForm
from administracion.models import TipoDeActividad
from usuario.mixin import has_permission

from django.contrib import messages

# Create your views here.
@has_permission
def home_administracion(request):
    template = loader.get_template("administracion/home_administracion.html")
    context = {"title": "Home Administracion"}
    return HttpResponse(template.render(context,request))

"""
    CRUD Tipos de actividad
"""
#pantalla principal de crud de tipos de actividades
@has_permission
def tipo_de_actividad_index(request):
    #queryset
    # tipo_de_actividad = TipoDeActividad.objects.filter(baja=False)

    if request.GET:
        snombre = request.GET['nombre']
        qs_tipos_de_actividad = TipoDeActividad.objects.filter(nombre=snombre)
    else:
        qs_tipos_de_actividad = TipoDeActividad.objects.all

    return render(request,'administracion/tipo_de_actividad/index.html',{'qs_tipos_de_actividad':qs_tipos_de_actividad})

###################### CLASS VIEW ###################

class TipoDeActividadIndexListView(ListView):
    model = TipoDeActividad
    context_object_name = 'qs_tipos_de_actividad'
    template_name = 'administracion/tipo_de_actividad/index.html'
    ordering = ['nombre']
    paginate_by = 6

    def get_queryset(self):
        if (self.request.method == 'GET' and self.request.GET and self.request.GET['nombre']):
            snombre = self.request.GET['nombre']
            return TipoDeActividad.objects.filter(nombre=snombre)
        else:
            return TipoDeActividad.objects.all()


#usa el formulario del modelo
# TO DO chequear posibles excepciones durante el save()
#TO DO implementar el softDelete()
class TipoDeActividadNuevoView(CreateView):
    model = TipoDeActividad
    form_class = TipoDeActividadForm
    template_name = 'administracion/tipo_de_actividad/nuevo.html'
    success_url = reverse_lazy('tipo_de_actividad_index_view')


class TipoDeActividadUpdateView(UpdateView):
    model = TipoDeActividad
    fields = ['nombre', 'titulo', 'subtitulo', 'descripcion', 'imagen_de_portada']
    template_name = 'administracion/tipo_de_actividad/editar.html'
    success_url = reverse_lazy('tipo_de_actividad_index_view')

#Por el momento esta funcion no hace nada. TO DO implementar softDelete( en models.py)
class TipoDeActividadDeleteView(DeleteView):
    model = TipoDeActividad
    template_name = 'administracion/tipo_de_actividad/eliminar.html'
    success_url = reverse_lazy('tipo_de_actividad_index_view')

@has_permission
def tipo_de_actividad_buscar(request):
    return render(request, "administracion/tipo_de_actividad/buscar.html")

# #usa el formulario del modelo
# #TO DO chequear posibles excepciones durante el save()
# #TO DO implementar el softDelete()
# def tipo_de_actividad_nuevo(request):
#     if(request.method=='POST'):
#         formulario = TipoDeActividadForm(request.POST, request.FILES)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect('tipo_de_actividad_index')
#     else:
#         formulario = TipoDeActividadForm()
#     return render(request,'administracion/tipo_de_actividad/nuevo.html',{'formulario':formulario})

# def tipo_de_actividad_editar(request, id_tipo_de_actividad):
#     try:
#         tipo_de_actividad = TipoDeActividad.objects.get(pk=id_tipo_de_actividad)
#         tipo_de_actividad = TipoDeActividad.objects.get(pk=id_tipo_de_actividad)
#     except TipoDeActividad.DoesNotExist:
#         # return render(request,'administracion/404_admin.html')
#         return redirect('tipo_de_actividad_index')

#     if(request.method=='POST'):
#         formulario = TipoDeActividadForm(request.POST,request.FILES, instance=tipo_de_actividad)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect('tipo_de_actividad_index')
#     else:
#         formulario = TipoDeActividadForm(instance=tipo_de_actividad)
#     return render(request,'administracion/tipo_de_actividad/editar.html',{'formulario':formulario})

# #TO DO implementar softDelete(en models.py)
# def tipo_de_actividad_eliminar(request,id_tipo_de_actividad):
#     try:
#         tipo_de_actividad = TipoDeActividad.objects.get(pk=id_tipo_de_actividad)
#     except TipoDeActividad.DoesNotExist:
#         # return render(request,'administracion/404_admin.html')
#         Warning("Tipo de actividad no encontrado")
#         return redirect('tipo_de_actividad_index')
#     tipo_de_actividad.delete()
#     return redirect('tipo_de_actividad_index')