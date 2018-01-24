from django.contrib import admin
from .models import Formulario


class AdminFormulario(admin.ModelAdmin):
    list_display = ["__str__", "Nombre", "Timestamp", "Mensaje"]
    class Meta:
        model = Formulario

admin.site.register(Formulario, AdminFormulario)
