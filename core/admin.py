
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Sede, Usuario

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'municipio', 'activa', 'fecha_creacion']
    list_filter = ['activa']
    search_fields = ['nombre', 'municipio']

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'nombre_completo', 'rol', 'sede', 'is_active']
    list_filter = ['rol', 'sede', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Información CCRF', {
            'fields': ('rol', 'sede')
        }),
    )

    def nombre_completo(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    nombre_completo.short_description = 'Nombre'