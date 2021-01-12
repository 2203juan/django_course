from django.urls import path, include
from . import views

app_name = 'skills'

urlpatterns = [
    path('', views.skills, name = "skills"),
    path('en/', views.skills_eng, name = "skills_eng"),
]