from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from administracion.forms import TipoDeActividadForm
from administracion.models import TipoDeActividad

from django.contrib import messages

# Create your views here.
def home_administracion(request):
    template = loader.get_template("administracion/home_administracion.html")
    context = {"title": "Home Administracion"}
    return HttpResponse(template.render(context,request))

"""
    CRUD Tipos de actividad
"""
#pantalla principal de crud de tipos de actividades
def tipo_de_actividad_index(request):
    #queryset
    # tipo_de_actividad = TipoDeActividad.objects.filter(baja=False)

    if request.GET:
        # ['nombre']:
        snombre = request.GET['nombre']
        qs_tipos_de_actividad = TipoDeActividad.objects.filter(nombre=snombre)
    else:
        qs_tipos_de_actividad = TipoDeActividad.objects.all

    return render(request,'administracion/tipo_de_actividad/index.html',{'qs_tipos_de_actividad':qs_tipos_de_actividad})

#usa el formulario del modelo
#TO DO chequear posibles excepciones durante el save()
#TO DO implementar el softDelete()
def tipo_de_actividad_nuevo(request):
    if(request.method=='POST'):
        formulario = TipoDeActividadForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('tipo_de_actividad_index')
    else:
        formulario = TipoDeActividadForm()
    return render(request,'administracion/tipo_de_actividad/nuevo.html',{'formulario':formulario})

def tipo_de_actividad_editar(request, id_tipo_de_actividad):
    try:
        tipo_de_actividad = TipoDeActividad.objects.get(pk=id_tipo_de_actividad)
        tipo_de_actividad = TipoDeActividad.objects.get(pk=id_tipo_de_actividad)
    except TipoDeActividad.DoesNotExist:
        # return render(request,'administracion/404_admin.html')
        return redirect('tipo_de_actividad_index')

    if(request.method=='POST'):
        formulario = TipoDeActividadForm(request.POST,request.FILES, instance=tipo_de_actividad)
        if formulario.is_valid():
            formulario.save()
            return redirect('tipo_de_actividad_index')
    else:
        formulario = TipoDeActividadForm(instance=tipo_de_actividad)
    return render(request,'administracion/tipo_de_actividad/editar.html',{'formulario':formulario})

#Por el momento esta funcion no hace nada. TO DO implementar softDelete( en models.py)
def tipo_de_actividad_eliminar(request,id_tipo_de_actividad):
    try:
        tipo_de_actividad = TipoDeActividad.objects.get(pk=id_tipo_de_actividad)
    except TipoDeActividad.DoesNotExist:
        # return render(request,'administracion/404_admin.html')
        Warning("Tipo de actividad no encontrado")
        return redirect('tipo_de_actividad_index')
    tipo_de_actividad.delete()
    return redirect('tipo_de_actividad_index')


def tipo_de_actividad_buscar(request):
    return render(request, "administracion/tipo_de_actividad/buscar.html")