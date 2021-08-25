from django.db import models

# Create your models here.
class Alumnos(models.Model):
    idAlumno = models.IntegerField(null=False,unique=True)
    nombreAlumno = models.TextField(max_length=60, default="",null=False)
    apellidoAlumno = models.TextField(max_length=80, default="",null=False)
    dniAlumno = models.CharField(max_length=8,null=False,unique=True)
    fechanacAlumno = models.DateField(null=False)
    edadAlumno = models.IntegerField(null=False)
    gradoAlumno = models.TextField(max_length=20,default="",null=False)
    seccionAlumno = models.CharField(max_length=1,default="",null=False)
    sexoAlumno =models.CharField(max_length=1,null=False)

class Apoderados(models.Model):
    idApoderados = models.IntegerField(null=False,unique=True)
    nombreApoderados = models.TextField(max_length=60, default="",null=False)
    apellidosApoderados = models.TextField(max_length=60, default="",null=False)
    dniApoderados = models.CharField(max_length=8,null=False,unique=True)
    domicilioApoderados = models.TextField(max_length=100,default="",null=False)
    sexoApoderados =models.CharField(max_length=1,null=False)