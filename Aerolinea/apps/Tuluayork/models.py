from django.db import models


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 200, blank= False, null= False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre



class Vuelos(models.Model):
    id = models.AutoField(primary_key=True)
    aerolinea = models.CharField(max_length= 200, blank= False, null= False)
    costo = models.IntegerField(blank= False, null= False)
    NoCupos = models.IntegerField(blank= False, null= False)
    fechaSalida = models.DateField(max_length= 200, blank= False, null= False)
    fechaLlegada = models.DateField(max_length= 200, blank= False, null= False)
    horaSalida = models.TimeField(max_length= 200, blank= False, null= False)
    horaLlegada = models.TimeField(max_length= 200, blank= False, null= False)
    LugarSalida = models.CharField(max_length= 200, blank= False, null= False)
    Destino = models.CharField(max_length= 200, blank= False, null= False)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Vuelo'
        verbose_name_plural = 'Vuelos'
        ordering = ['aerolinea']

    def __str__(self):
        return self.aerolinea
        


class Cliente(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length= 100, blank= False, null= False)
    apellido = models.CharField(max_length= 100, blank= False, null= False)
    edad = models.IntegerField(blank= False, null= False)
    fechaNacimiento = models.DateField(max_length= 200, blank= False, null= False)
    ciudadResidencia = models.CharField(max_length= 100, blank= False, null= False)
    tipoUsuario = models.ForeignKey(Usuario, on_delete = models.CASCADE, null= True)
    idVuelo = models.ManyToManyField(Vuelos, null= True)
    estado = models.BooleanField('Estado', default = True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    idVuelo = models.ForeignKey(Vuelos, on_delete = models.CASCADE)
    idCliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fechaHoraReserva = models.DateTimeField(blank= False, null= False)
    idFuncionario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['id']
    
    def __str__(self):
        return self.id

   
    

    

