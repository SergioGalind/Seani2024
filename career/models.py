from django.db import models

# Create your models here.
class Career(models.Model):
    LEVELS=[
        ('TSU', 'Tecnico superior universitario'),
        ('Ing', 'Ingenieria'),
        ('Lic', 'Licenciatura'),
        ('M', 'Maestria'),
    ]
    level = models.CharField(
    verbose_name = "nivel",
    max_length=20,
    choices = LEVELS
)
    name = models.CharField(
        verbose_name = "Nombre",
        max_length=150,
        )
    short_name = models.CharField (
        verbose_name ="Abrreviatura", 
        max_length=20
    )   

    def __str__(self):
        return f" {self.level} {self.short_name}"
    class Meta:
        verbose_name="Carrera"
        verbose_name_plural="Carreras"
