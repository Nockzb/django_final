from django.db import models

# Create your models here.
# Modelo Deporte
class Deporte(models.Model):
    id_deporte = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)        
        
    class Meta:        
        verbose_name_plural = "Deportes"
        db_table = "deportes"
        def __str__(self):
            return f"{self.id_deporte} {self.nombre}"
        
# Modelo Instalacion
class Instalacion(models.Model):
    id_instalacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length = 50)      
    direccion = models.CharField(max_length=100)
    iluminacion = models.BooleanField(default=False)
    cubierta = models.BooleanField(default=False)
    class Meta:        
        verbose_name_plural = "Instalaciones"
        db_table = "instalaciones"
        def __str__(self):
            return f"{self.id_instalacion} {self.nombre} {self.nombre} {self.direccion} {self.iluminacion} {self.cubierta}"
        
# TODO: DESDE ACA
# Modelo Equipo
class Equipo(models.Model):
    id_equipo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    id_deporte = models.ForeignKey('Deporte', on_delete=models.RESTRICT, db_column='id_deporte')
    equipacion_principal = models.CharField(max_length=100)
    equipacion_suplente = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Equipos"
        db_table = "equipos"

    def __str__(self):
        return f"{self.id_equipo} {self.nombre} {self.id_deporte} {self.equipacion_principal} {self.equipacion_suplente} {self.contacto} {self.telefono} {self.email}"

# Modelo Jugador
class Jugador(models.Model):
    id_jugador = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50, blank=True, null=True)
    id_equipo = models.ForeignKey('Equipo', on_delete=models.RESTRICT, db_column='id_equipo')
    dorsal = models.IntegerField()
    fecha_nacimiento = models.DateField()
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    peso = models.PositiveIntegerField()
    telefono = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Jugadores"
        db_table = "jugadores"
        unique_together = ['id_equipo', 'dorsal']  # Índice para evitar duplicados

    def __str__(self):
        return f"{self.id_jugador} {self.nombre} {self.apellido1} {self.apellido2} {self.id_equipo} {self.dorsal} {self.fecha_nacimiento} {self.altura} {self.peso} {self.telefono}"