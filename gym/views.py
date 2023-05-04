from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from gym.forms import ContactoForm

# Create your views here.
def home(request):
    template = loader.get_template("gym/home.html")
    context = {"title": "Home"}
    return HttpResponse(template.render(context, request))


def contacto(request):
    mensaje=None
    if(request.method=='GET'):
        contacto_form = ContactoForm()
        return render(request,'gym/contact.html',{
            'contacto_form': contacto_form
        })

    else:
        contacto_form= ContactoForm(request.POST)
        if(contacto_form.is_valid()):  
            messages.success(request,'¡Mensaje enviado con éxito, responderemos a la brevedad!')  
            contacto_form = ContactoForm()
        else:
            messages.warning(request,'Por favor verificá los errores marcados antes de enviar')
    
    return render(request,'gym/contact.html',{
                    'mensaje': mensaje,
                    'contacto_form': contacto_form})


def loguearse(request):
   
    return render(request, 'gym/contact.html',{
        'form': UserCreationForm
    })


def sing_up(request):
    template = loader.get_template("gym/sing_up.html")
    context = {"title": "Sing Up"}
    return HttpResponse(template.render(context, request))

