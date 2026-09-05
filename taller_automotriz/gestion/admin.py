from django.contrib import admin
from .models import Cliente, Vehiculo, TipoServicio, Servicio

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'telefono')
    search_fields = ('rut', 'apellido')

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('patente', 'marca', 'modelo', 'cliente')
    # Habilita un buscador por patente o RUT del dueño
    search_fields = ('patente', 'cliente__rut') 

@admin.register(TipoServicio)
class TipoServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_referencial')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'fecha', 'estado', 'costo_total')
    list_filter = ('estado', 'fecha')
    # Transforma la relación N:M en un selector de doble caja muy fácil de usar
    filter_horizontal = ('tipos_de_servicio',)