from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

from django.views.generic import View, CreateView, ListView,UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from .form_autenticacion import FormularioLogin, FormularioUsuario
from usuario.models import Usuario
from usuario.mixin import LoginYSuperUsuarioMixin


class RegistrarUsuario(CreateView):
    model = Usuario
    form_class= FormularioUsuario
    template_name = 'usuario/registrar_usuario.html'
    success_url = reverse_lazy('home')

    def post(self,request,*args, **kwargs):
        form= self.form_class(request.POST)
        print("entro a registro")
        
        if form.is_valid():
            print("formulario valido")
            nuevo_usuario=Usuario(
                email = form.cleaned_data.get('email'),
                username = form.cleaned_data.get('username'),
                nombre = form.cleaned_data.get('nombre'),
                apellido = form.cleaned_data.get('apellido'),
                documento = form.cleaned_data.get('documento')
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            print("guarda el usuario")
            nuevo_usuario.save()
            return redirect('home')
        else: 
            print("no es valido")
            return render(request, self.template_name, {'form':form})


def cerrar_sesion(request):
    logout(request)

    return redirect('home')

def loguear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contrasenia=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contrasenia)
            if usuario is not None:
                login(request,usuario)
                return redirect('home')
            else:
                messages.error(request, "usuario no válido")
        else:
                messages.error(request, "Información erronea")

    form=AuthenticationForm()
    return render(request, "usuario/login.html",{"form":form})

#login personalizado

class Login(FormView):
    template_name ='usuario/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:

            return super(Login.self).dispatch(request,*args,**kwargs)
    print("entro a login")    
    def form_valid(self,form):
        print("formulario login valido")
        login(self.request, form.get_user())
        return super(Login,self).form_valid(form)
    
def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('home')


class ListadoUsuario(LoginYSuperUsuarioMixin, ListView):
    model = Usuario
    template_name = 'usuario/listar_usuarios.html'
    
    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)
  
class EliminarUsuario(LoginYSuperUsuarioMixin, DeleteView):
    model = Usuario
    template_name = 'usuario/eliminar_usuario.html'
    success_url = reverse_lazy('listar_usuarios')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()  
        return HttpResponseRedirect(self.get_success_url())
    
   
    
   