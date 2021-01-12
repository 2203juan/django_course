from django.db import models

# Create your models here.
class HardSkill(models.Model):
    title = models.CharField(max_length = 100)
    def __str__(self):
        return self.title

class SoftSkill(models.Model):
    title = models.CharField(max_length = 100)
    def __str__(self):
        return self.title

class ProgrammingLang(models.Model):
    title = models.CharField(max_length = 100)
    level = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = "skills/images/")

    def __str__(self):
        return self.title

class Other(models.Model):
    title = models.CharField(max_length = 100)
    level = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = "skills/images/")

    def __str__(self):
        return self.title

class Tecnica(models.Model):
    titulo = models.CharField(max_length = 100)
    def __str__(self):
        return self.titulo

class Blanda(models.Model):
    titulo = models.CharField(max_length = 100)
    def __str__(self):
        return self.titulo