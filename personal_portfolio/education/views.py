from django.shortcuts import render, get_object_or_404
from .models import Education

# Create your views here.
def education(request):
    education = Education.objects.all()
    return render(request,"education/education.html", {"education": education})

def education_eng(request):
    education = Education.objects.all()
    return render(request,"education/education_eng.html", {"education": education})