from django import forms
from .models import TipoDeActividad

class TipoDeActividadForm(forms.ModelForm):

    class Meta:
        model=TipoDeActividad
        fields=['nombre','titulo','subtitulo','descripcion','imagen_de_portada']


    # se pueden agregar validators
    nombre=forms.CharField(
            label='Nombre', 
            widget=forms.TextInput(attrs={'class':'form-control'})
        )

    titulo=forms.CharField(
            label='Título', 
            widget=forms.TextInput(attrs={'class':'form-control'})
        )

    subtitulo=forms.CharField(
            label='Subtítulo', 
            widget=forms.TextInput(attrs={'class':'form-control'})
        )

    descripcion = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )

    imagen_de_portada = forms.ImageField(
        widget=forms.FileInput(attrs={'class':'form-control'})
    )