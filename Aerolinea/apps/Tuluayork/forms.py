from django import forms
from .models import Usuario, Vuelos, Cliente,Reserva

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula', 'nombre','apellido', 'edad','fechaNacimiento', 'ciudadResidencia', 'tipoUsuario']

class VuelosForm(forms.ModelForm):
    class Meta:
        model = Vuelos
        fields = ['aerolinea', 'costo', 'NoCupos','fechaSalida', 'fechaLlegada','horaSalida', 'horaLlegada', 'LugarSalida','Destino']

