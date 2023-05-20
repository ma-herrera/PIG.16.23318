from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from gym.forms import ContactoForm

# from .forms_registro import RegistroForm


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



def actividades(request):
    return render(request, 'gym/actividades.html')



def actividades(request):
    return render(request, 'gym/actividades.html')



########### prueba de formulario de registro

# def registro(request):
#     if request.method == 'POST':
#         form = RegistroForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('inicio')  
#     else:
#         form = RegistroForm()
    
#     return render(request, 'register.html', {'form': form})
    
