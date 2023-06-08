from django import forms
from .models import TipoDeActividad, Profesor, Cliente, TipoDocumento

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
    
######################################################################

class ProfesorForm(forms.ModelForm):

    class Meta:
        model: Profesor
        fields=["apellido", "nombre", "tipoDocumento", "numeroDocumento", "telefono", 'email', 'coberturaMedica', 'numeroAfiliado', 'cuil', 'fechaAlta', 'fechaBaja']

    apellido = forms.CharField(
        label = 'Apellido',
        widget = forms.TextInput(attrs={'class':'form-control'})
        )

    nombre = forms.CharField(
        label = 'Nombre',
        widget = forms.TextInput(attrs={'class':'form-control'})
        )
    
    tipoDocumento = forms.ModelChoiceField(
        queryset=TipoDocumento.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    numeroDocumento = forms.IntegerField(
        label="Número de documento",
        widget= forms.TextInput(attrs={'class':'form-control'})
        )
    
    telefono = forms.CharField(
        label="telefono",
        widget= forms.TextInput(attrs={'class':'form-control'})
        )

    email = forms.CharField(
        label = 'E-mail',
        widget = forms.TextInput(attrs={'class':'form-control'})
        )
    
    coberturaMedica = forms.CharField(
        label = 'Cobertura médica',
        widget = forms.TextInput(attrs={'class':'form-control'})
        )
    
    numeroAfiliado = forms.CharField(
        label = 'Número de afiliado',
        widget = forms.TextInput(attrs={'class':'form-control'})
        )

    cuil = forms.IntegerField(
        label="Cuil",
        widget= forms.TextInput(attrs={'class':'form-control'})
        )

    fechaAlta = forms.DateField(
            label='Fecha Inicio', 
            widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
        )

    fechaBaja = forms.DateField(
            label='Fecha de Baja', 
            widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
        )
