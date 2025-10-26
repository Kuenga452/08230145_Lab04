
from django.shortcuts import render
from .models import LearningJourney, AboutMe

def index(request):
    # Get all learning journeys and about me data
    journeys = LearningJourney.objects.all()
    about_people = AboutMe.objects.all()  # Get all AboutMe entries
    
    context = {
        'journeys': journeys,
        'about_people': about_people,
    }
    return render(request, 'index.html', context)

def about_me(request):
    # Get all about me data
    about_people = AboutMe.objects.all()  # Get all AboutMe entries
    
    context = {
        'about_people': about_people,
    }
    return render(request, 'aboutMe.html', context)