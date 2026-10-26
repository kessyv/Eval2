from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=100, unique=True)

    class Meta: verbose_name_plural = 'Categorias'
    ordering = ['nombre',]
    def __str__(self):
        return f"{self.nombre} {self.tipo}"

class Cuenta (models.Model):
    usuario = models.CharField(max_length=80, unique=True)
    correo = models.CharField(max_length=120)

    class Meta: verbose_name_plural = 'Cuentas'
    ordering = ['usuario',]
    def __str__(self):
        return f"{self.usuario} {self.correo}"

class Personaje(models.Model):
    raza = models.CharField(max_length=20)
    descripcion = models.TextField(200)
    nivel = models.PositiveIntegerField()
    ban = models.BooleanField(False)
    creado= models.DateTimeField(auto_now_add=True)

    class Meta: verbose_name_plural = 'Personajes'
    ordering = ['raza',]
    def __str__(self):
        return f"{self.raza} {self.descripcion}"

class Items(models.Model):
    id = models.AutoField(primary_key=True)
    personaje_id = models.ForeignKey(Personaje,on_delete=models.CASCADE)
    categoria_id = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField()

    class Meta: verbose_name_plural = 'Items'
    ordering = ['nombre',]
    def __str__(self):
        return f"{self.nombre} {self.descripcion}"

class CuentaPersonaje(models.Model):
    id = models.AutoField(primary_key=True)
    cuenta_id = models.ForeignKey(Cuenta,on_delete=models.CASCADE)
    personaje_id = models.ForeignKey(Personaje,on_delete=models.CASCADE)
    personaje_id = models.ForeignKey(Personaje,on_delete=models.CASCADE)

    class Meta: verbose_name_plural = 'CuentaPersonajes'
    ordering = ['cuenta_id',]
    def __str__(self):
        return f"{self.cuenta_id} {self.personaje_id}"












