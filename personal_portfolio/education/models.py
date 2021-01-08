from django.db import models

# Create your models here.
class Education(models.Model):
    title = models.CharField(max_length = 100)
    date_start = models.CharField(max_length = 50)
    date_end = models.CharField(max_length = 50)
    institution = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = "eduaction/images/")
    url = models.URLField(blank = True)

    def __str__(self):
        return self.title