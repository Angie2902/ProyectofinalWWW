from django.urls import path 
from .views import crearCliente, ListarVuelos, editarCliente, ListarClientes,crearVuelo, ListarVuelos, editarVuelo, EliminarVuelo, EliminarCliente


urlpatterns = [

    path('crear_cliente/', crearCliente, name ='crear_cliente'),
    path('listar_clientes/', ListarClientes, name ='listar_clientes'),
    path('editar_cliente/<int:cedula>', editarCliente, name ='editar_cliente'),
    path('eliminar_cliente/<int:cedula>', EliminarCliente, name ='eliminar_cliente'),
    path('crear_vuelo/', crearVuelo, name ='crear_vuelo'),
    path('listar_vuelos/', ListarVuelos, name ='listar_vuelos'),
    path('editar_vuelo/<int:id>', editarVuelo, name ='editar_vuelo'),
    path('eliminar_vuelo/<int:id>', EliminarVuelo, name ='eliminar_vuelo'),
   
    



]