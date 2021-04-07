from django.contrib import admin
from .models import Vuelos, Cliente, Reserva, Usuario

admin.site.register(Vuelos)
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Usuario)
