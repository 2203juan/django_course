from django.urls import path, include
from . import views

app_name = 'education'

urlpatterns = [
    path('', views.education, name = "education"),
    path('en/', views.education_eng, name = "education_eng"),
]