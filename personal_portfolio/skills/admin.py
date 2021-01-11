from django.contrib import admin

# Register your models here.
from .models import HardSkill, SoftSkill, ProgrammingLang, Other

admin.site.register(HardSkill)

admin.site.register(SoftSkill)

admin.site.register(ProgrammingLang)

admin.site.register(Other)
