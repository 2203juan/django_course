from django.shortcuts import render
from .models import Project
from education.models import Education

# Create your views here.
def home(request):
    education = Education.objects.all()
    return render(request,"portfolio/home.html", {"education": education})

def portfolio(request):
    fetch = Project.objects.all()
    return render(request,"portfolio/portfolio.html",{"projects": fetch})