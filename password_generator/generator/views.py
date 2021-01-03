from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,"generator/home.html")

def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    size = int(request.GET.get("length"))

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    
    if request.GET.get("number"):
        characters.extend(list("0123456789"))
    
    if request.GET.get("special"):
        characters.extend(list("!#$%&/()=?¡*;.)"))
    
    

    password_ = ""


    for _ in range(size):
        password_ += random.choice(characters)


    return render(request,"generator/password.html", {"password": password_})