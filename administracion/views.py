from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from administracion.forms import TipoDeActividadForm, ProfesorForm, ClienteForm
from administracion.models import TipoDeActividad, Profesor, Persona, Cliente
from usuario.mixin import has_permission, LoginYSuperUsuarioMixin

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
    
    if request.GET:
        snombre = request.GET['nombre']
        qs_tipos_de_actividad = TipoDeActividad.objects.filter(nombre=snombre)
    else:
        qs_tipos_de_actividad = TipoDeActividad.objects.all

    return render(request,'administracion/tipo_de_actividad/index.html',{'qs_tipos_de_actividad':qs_tipos_de_actividad})

###################### CLASS VIEW ###################

class TipoDeActividadIndexListView(LoginYSuperUsuarioMixin,ListView):
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

class TipoDeActividadNuevoView(LoginYSuperUsuarioMixin,CreateView):
    model = TipoDeActividad
    form_class = TipoDeActividadForm
    template_name = 'administracion/tipo_de_actividad/nuevo.html'
    success_url = reverse_lazy('tipo_de_actividad_index_view')


class TipoDeActividadUpdateView(LoginYSuperUsuarioMixin,UpdateView):
    model = TipoDeActividad
    fields = ['nombre', 'titulo', 'subtitulo', 'descripcion', 'imagen_de_portada']
    template_name = 'administracion/tipo_de_actividad/editar.html'
    success_url = reverse_lazy('tipo_de_actividad_index_view')

class TipoDeActividadDeleteView(LoginYSuperUsuarioMixin,DeleteView):
    model = TipoDeActividad
    template_name = 'administracion/tipo_de_actividad/eliminar.html'
    success_url = reverse_lazy('tipo_de_actividad_index_view')

@has_permission
def tipo_de_actividad_buscar(request):
    return render(request, "administracion/tipo_de_actividad/buscar.html")

############################## PROFESOR ##################################

class ProfesorIndexListView(LoginYSuperUsuarioMixin,ListView):
    model = Profesor
    context_object_name = 'qs_profesor'
    template_name = 'administracion/profesor/index.html'
    ordering = ['apellido', 'nombre']
    paginate_by = 6

    def get_queryset(self):
        if (self.request.method == 'GET' and self.request.GET and self.request.GET['apellido']):
            sapellido = self.request.GET['apellido']
            return Profesor.objects.filter(apellido=sapellido)
        else:
            return Profesor.objects.all()

class ProfesorNuevoView(LoginYSuperUsuarioMixin,CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'administracion/profesor/nuevo.html'
    success_url = reverse_lazy('profesor_index_view')


class ProfesorUpdateView(LoginYSuperUsuarioMixin,UpdateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'administracion/profesor/editar.html'
    success_url = reverse_lazy('profesor_index_view')

class ProfesorDeleteView(LoginYSuperUsuarioMixin,DeleteView):
    model = Profesor
    template_name = 'administracion/profesor/eliminar.html'
    success_url = reverse_lazy('profesor_index_view')

@has_permission
def profesor_buscar(request):
    return render(request, "administracion/profesor/buscar.html")


############################## CLIENTE ##################################

class ClienteIndexListView(LoginYSuperUsuarioMixin,ListView):
    model = Cliente
    context_object_name = 'qs_cliente'
    template_name = 'administracion/cliente/index.html'
    ordering = ['apellido', 'nombre']
    paginate_by = 6

    def get_queryset(self):
        if (self.request.method == 'GET' and self.request.GET and self.request.GET['apellido']):
            sapellido = self.request.GET['apellido']
            return Cliente.objects.filter(apellido=sapellido)
        else:
            return Cliente.objects.all()

class ClienteNuevoView(LoginYSuperUsuarioMixin,CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'administracion/cliente/nuevo.html'
    success_url = reverse_lazy('cliente_index_view')


class ClienteUpdateView(LoginYSuperUsuarioMixin,UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'administracion/cliente/editar.html'
    success_url = reverse_lazy('cliente_index_view')

class ClienteDeleteView(LoginYSuperUsuarioMixin,DeleteView):
    model = Cliente
    template_name = 'administracion/cliente/eliminar.html'
    success_url = reverse_lazy('cliente_index_view')

@has_permission
def cliente_buscar(request):
    return render(request, "administracion/cliente/buscar.html")


