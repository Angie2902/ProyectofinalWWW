from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ClienteForm, VuelosForm
from .models import Vuelos, Cliente

def Home(request):
    return render(request, 'index.html')



"""---------------------CRUDS CLIENTE-------------------------"""

def crearCliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('index')
    else:
        cliente_form = ClienteForm()
    return render(request, 'Tuluayork/crear_cliente.html', {'cliente_form':cliente_form})

def editarCliente(request, cedula):

    cliente_form = None
    error = None

    try:
        cliente = Cliente.objects.get(cedula = cedula)
        if request.method == 'GET':
            cliente_form = ClienteForm(instance = cliente)
        else:
            cliente_form = ClienteForm(request.POST, instance = cliente)
            if cliente_form.is_valid():
                cliente_form.save()
            return redirect('index')
    
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'Tuluayork/crear_cliente.html', {'cliente_form': cliente_form, 'error': error})

def ListarClientes(request):
    clientes = Cliente.objects.filter(estado = True) 
    return render(request, 'Tuluayork/listar_clientes.html', {'clientes':clientes})

def EliminarCliente(request, cedula):
    cliente = Cliente.objects.get(cedula=cedula)
    if request.method == 'POST':
        cliente.estado = False
        cliente.save()
        return redirect('Tuluayork:listar_clientes')
    return render(request, 'Tuluayork/eliminar_cliente.html', {'cliente':cliente})

"""---------------------CRUDS VUELOS-------------------------"""


def crearVuelo(request):
    if request.method == 'POST':
        vuelo_form = VuelosForm(request.POST)
        if vuelo_form.is_valid():
            vuelo_form.save()
            return redirect('index')
    else:
        vuelo_form = VuelosForm()
    return render(request, 'Tuluayork/crear_vuelo.html', {'vuelo_form':vuelo_form})

def editarVuelo(request, cedula):

    vuelo_form = None
    error = None

    try:
        vuelo = Vuelos.objects.get(cedula = cedula)
        if request.method == 'GET':
            vuelo_form = VuelosForm(instance = vuelo)
        else:
            vuelo_form = VuelosForm(request.POST, instance = vuelo)
            if vuelo_form.is_valid():
                vuelo_form.save()
            return redirect('index')
    
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'Tuluayork/crear_vuelo.html', {'vuelo_form': vuelo_form, 'error': error})

def ListarVuelos(request):
    vuelos = Vuelos.objects.filter( estado = True) 
    return render(request, 'Tuluayork/listar_vuelos.html', {'vuelos':vuelos})

def EliminarVuelo(request, id):
    vuelo = Vuelos.objects.get(id=id)
    if request.method == 'POST':
        vuelo.estado = False
        vuelo.save()
        return redirect('Tuluayork:listar_vuelos')
    return render(request, 'Tuluayork/eliminar_vuelo.html', {'vuelo':vuelo})

"""---------------------CRUDS RESERVAS-------------------------"""