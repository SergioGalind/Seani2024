from django.db import models

# Create your models here.
class Module(models.Model):
    name = models.CharField(
        verbose_name = 'Nombre del Módulo',
        max_length = 30)
    description = models.CharField(
        verbose_name = 'Descripción del Módulo',
        max_length = 100)
    def _str_(self):
        return self.name

class Question(models.Model):
    module = models.ForeignKey(Module, on_delete = models.CASCADE)
    question_text = models.CharField(
        null = True, blank = True,
        verbose_name = "Texto de la Pregunta",
        max_length = 255)
    question_image = models.ImageField(
        null = True, blank = True,
        verbose_name = "Imagen de la Pregunta",
        upload_to='questions')
    answer1 = models.CharField(
        verbose_name = "Respuesta A",
        max_length = 150)
    answer2 = models.CharField(
        verbose_name = "Respuesta B",
        max_length = 150)
    answer3 = models.CharField(
        null = True, blank = True,
        verbose_name = "Respuesta C",
        max_length = 150)
    answer4 = models.CharField(
        null = True, blank = True,
        verbose_name = "Respuesta D",
        max_length = 150)
    correct = models.CharField(
        verbose_name = "Respuesta Correcta",
        max_length = 5)
    
    def _str_(self):
        return f"{ self.module.name }  Pregunta  { self.id }"
