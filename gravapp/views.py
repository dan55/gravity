from django.shortcuts import render

from gravapp.models import Character
# Create your views here.

def index(request):
    characters = Character.objects.all()
    nodes, links = [], []

    for character in characters:
        nodes.append({ 'name': str(character.first_name) })

    context = { 'nodes': nodes, 'links': links }

    return render(request, 'index.html', { 'context': context })
