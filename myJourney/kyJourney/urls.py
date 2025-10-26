from django.urls import path
from . import views

app_name = 'kyJourney'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_me, name='about_me'),  # <-- new URL
]