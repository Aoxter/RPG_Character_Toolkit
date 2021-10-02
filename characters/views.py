from django.shortcuts import render
from characters.models import Character


characters = [
    {
        'author': "Piotr",
        'name': 'Stefano',
        'system': 'WeirdWorld',
        'description': 'Mighty Stefano, the hero of whole WeirdWorld',
        'date_created': '10.09.2021',
        'last_update': '12.09.2021'
    },
    {
        'author': "Piotr",
        'name': 'Orlan',
        'system': 'Blades in the Dark',
        'description': 'Fallen nobleman who wants only one thing - reclaim his status and power',
        'date_created': '10.08.2019',
        'last_update': '10.08.2019'
    }
]


def index(request):
    context = {
        #'characters': characters
        'characters': Character.objects.all()
    }
    return render(request, 'characters/index.html', context)


def about(request):
    return render(request, 'characters/about.html', {'title': 'About'})