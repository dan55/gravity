from django.http import HttpResponse
from django.shortcuts import render

from gravapp.models import Character
from .forms import CharacterForm

from django.views.decorators.csrf import csrf_exempt

def index(request):
    characters = Character.objects.all()
    nodes, links = [], []

    for character in characters:
        nodes.append({ 'name': str(character.first_name) })

    context = { 'nodes': nodes, 'links': links }
    form = CharacterForm()

    return render(request, 'index.html', { 'context': context, 'form': form })

@csrf_exempt
def create_character(request):
    return HttpResponse('Success');