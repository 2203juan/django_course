from django.shortcuts import render
from .models import HardSkill, SoftSkill, ProgrammingLang, Other, Tecnica, Blanda

# Create your views here.
def skills(request):
    hard, soft, lang, others = Tecnica.objects.all(), Blanda.objects.all(), ProgrammingLang.objects.all(), Other.objects.all()
    return render(request,"skills/skills_spanish.html", {"hard": hard,"soft":soft, "lang":lang,"others":others})

def skills_eng(request):
    hard, soft, lang, others = HardSkill.objects.all(), SoftSkill.objects.all(), ProgrammingLang.objects.all(), Other.objects.all()
    return render(request,"skills/skills.html", {"hard": hard,"soft":soft, "lang":lang,"others":others})

