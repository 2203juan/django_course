from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    return render(request,"portfolio/home.html")

def portfolio(request):
    fetch = Project.objects.all()
    return render(request,"portfolio/portfolio.html",{"projects": fetch})