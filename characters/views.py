from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from characters.models import Character


@ login_required()
def home(request):
    context = {
        'characters': Character.objects.all()
    }
    return render(request, 'characters/home.html', context)


def about(request):
    return render(request, 'characters/about.html', {'title': 'About'})