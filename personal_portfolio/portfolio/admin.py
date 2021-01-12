from django.contrib import admin

# Register your models here.
from .models import Project, ProjectSpanish

admin.site.register(Project)
admin.site.register(ProjectSpanish)
