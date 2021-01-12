from django.contrib import admin

# Register your models here.
from .models import HardSkill, SoftSkill, ProgrammingLang, Other, Tecnica, Blanda

admin.site.register(HardSkill)

admin.site.register(SoftSkill)

admin.site.register(ProgrammingLang)

admin.site.register(Other)

admin.site.register(Tecnica)

admin.site.register(Blanda)