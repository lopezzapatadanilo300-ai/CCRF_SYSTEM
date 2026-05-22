from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True)
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'sede'


class Usuario(AbstractUser):
    ROL_CHOICES = [
        ('pastor_central', 'Pastor Central'),
        ('pastor_sede', 'Pastor Sede'),
        ('secretario', 'Secretario'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='secretario')
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.rol}"

    class Meta:
        db_table = 'usuario'


class Miembro(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    ministerio = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        db_table = 'miembro'
        ordering = ['nombre_completo']


class MovimientoFinanciero(models.Model):
    TIPO_CHOICES = [
        ('diezmo', 'Diezmo'),
        ('ofrenda', 'Ofrenda'),
        ('primicia', 'Primicia'),
        ('accion_gracias', 'Acción de Gracias'),
         ('gasto', 'Gasto'),
    ]
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True)
    miembro = models.ForeignKey(Miembro, on_delete=models.SET_NULL, null=True, blank=True)
    registrado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.tipo == 'diezmo' and not self.miembro:
            raise ValidationError('El diezmo debe estar asociado a un miembro.')

    def __str__(self):
        return f"{self.tipo} - ${self.monto} - {self.fecha}"

    class Meta:
        db_table = 'movimiento_financiero'
        ordering = ['-fecha']


class ReporteInventario(models.Model):
    ESTADO_CHOICES = [
        ('borrador', 'Borrador'),
        ('enviado', 'Enviado'),
        ('revisado', 'Revisado'),
    ]
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    mes = models.IntegerField()
    anio = models.IntegerField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='borrador')
    creado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    fecha_envio = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Inventario {self.mes}/{self.anio} - {self.sede}"

    class Meta:
        db_table = 'reporte_inventario'
        unique_together = ['sede', 'mes', 'anio']


class InventarioItem(models.Model):
    ESTADO_CHOICES = [
        ('bueno', 'Bueno'),
        ('regular', 'Regular'),
        ('malo', 'Malo'),
        ('baja', 'Dado de baja'),
    ]
    reporte = models.ForeignKey(ReporteInventario, on_delete=models.CASCADE, related_name='items')
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    cantidad = models.IntegerField(default=1)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='bueno')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'inventario_item'