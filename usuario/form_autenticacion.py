from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from usuario.models import Usuario

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super(FormularioLogin,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioUsuario(forms.ModelForm):
    """ Formulario de registro de un usuario en la base de datos"""

    password1 = forms.CharField(label='Constraseña', widget= forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese su contraseña',
            'id': 'password1',
            'required':'required',
        }
    ))
    password2 = forms.CharField(label='Constraseña de confirmación', widget= forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id': 'password2',
            'required':'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('username','email','nombre','apellido','documento')
        widget = {
            'email': forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Correo Electronico',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su apellido',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario',
                }
            ),
            'documento': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su DNI',
                }
            ),
        }
    def clean_password2(self):
        """ Validacion de contraseña antes de ser guardada"""
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 != password2:
           raise forms.ValidationError('Las contraseñas no coinciden!')
        return password2

    def save(self, commit= True):
        user =super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user