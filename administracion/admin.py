from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Profesor
from .models import TipoDocumento
from .models import Cliente
from .models import Horario
from .models import TipoDeActividad
from .models import Actividad
from .models import Inscripcion



admin.site.register(TipoDocumento)
admin.site.register(Cliente)
admin.site.register(Profesor)
admin.site.register(Horario)
admin.site.register(TipoDeActividad)
admin.site.register(Actividad)
admin.site.register(Inscripcion)