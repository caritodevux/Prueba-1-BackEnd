from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    correo = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, unique=True, verbose_name="Patente")
    marca = models.CharField(max_length=50, verbose_name="Marca")
    modelo = models.CharField(max_length=50, verbose_name="Modelo")
    anio = models.PositiveIntegerField(verbose_name="Año")
    color = models.CharField(max_length=30, verbose_name="Color")
    
    # Clave Foránea: Relación 1:N con Cliente
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT, related_name="vehiculos")

    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo}"

class TipoServicio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Servicio")
    descripcion = models.TextField(verbose_name="Descripción")
    # Usamos PositiveIntegerField para valores en pesos chilenos (sin decimales)
    precio_referencial = models.PositiveIntegerField(verbose_name="Precio Referencial")

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    ESTADOS = [
        ('ING', 'Ingresado'),
        ('REP', 'En reparación'),
        ('ESP', 'Esperando repuesto'),
        ('FIN', 'Finalizado'),
        ('ENT', 'Entregado'),
    ]

    fecha = models.DateField(verbose_name="Fecha del servicio")
    kilometraje = models.PositiveIntegerField(verbose_name="Kilometraje")
    descripcion = models.TextField(verbose_name="Descripción del trabajo")
    costo_total = models.PositiveIntegerField(verbose_name="Costo Total")
    estado = models.CharField(max_length=3, choices=ESTADOS, default='ING', verbose_name="Estado")
    
    # Clave Foránea: Relación 1:N con Vehiculo
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.RESTRICT, related_name="servicios")
    
    # Relación N:M: Django crea la tabla intermedia "Detalle_Servicio" automáticamente
    tipos_de_servicio = models.ManyToManyField(TipoServicio, related_name="servicios_realizados")

    def __str__(self):
        return f"Servicio a {self.vehiculo.patente} - {self.fecha}"