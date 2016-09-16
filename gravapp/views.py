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

@csrf_exempt # TODO: Don't do this
def create_character(request):
    post = request.POST
    first = str(post['first_name'])
    last = str(post['last_name'])
    character = Character(first_name=first, last_name=last)

    character.save()

    return HttpResponse('Success');

@csrf_exempt
def delete_character(request):
    post = request.POST

    Character.objects.filter(first_name__iexact=request.POST['name']).delete()

    return HttpResponse('Success');