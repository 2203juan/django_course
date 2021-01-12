from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 500)
    image = models.ImageField(upload_to = "portfolio/images/")
    url = models.URLField(blank = True)

    def __str__(self):
        return self.title

class ProjectSpanish(models.Model):
    titulo = models.CharField(max_length = 50)
    descripcion = models.TextField(max_length = 500)
    imagen = models.ImageField(upload_to = "portfolio/images/")
    url = models.URLField(blank = True)

    def __str__(self):
        return self.titulo