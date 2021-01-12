from django.shortcuts import render
from .models import Project, ProjectSpanish

# Create your views here.
# HOME
def home(request):
    return render(request,"portfolio/home.html")

def home_eng(request):
    return render(request,"portfolio/home_eng.html")

# PORTFOLIO
def portfolio(request):
    fetch = ProjectSpanish.objects.all()
    return render(request,"portfolio/portfolio.html",{"projects": fetch})

def portfolio_eng(request):
    fetch = Project.objects.all()
    return render(request,"portfolio/portfolio_eng.html",{"projects": fetch})