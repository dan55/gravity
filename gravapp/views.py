from django.http import HttpResponse
from django.shortcuts import render

from gravapp.models import Character, Relationship
from .forms import CharacterForm

from django.views.decorators.csrf import csrf_exempt

def index(request):
    characters = Character.objects.all()
    nodes, links = [], []

    for character in characters:
        nodes.append({ 'name': str(character.first_name) })

    for rel in Relationship.objects.all():
        source = str(rel.character_1.first_name)
        target = str(rel.character_2.first_name)

        links.append({ 'source': source, 'target': target })

    #links.append({ 'source': 0, 'target': 1 })

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

    return HttpResponse('Success')

@csrf_exempt
def delete_character(request):
    post = request.POST

    Character.objects.filter(first_name__iexact=request.POST['name']).delete()

    return HttpResponse('Success')

@csrf_exempt
def create_relationship(request):
    post = request.POST
    source = str(post['source'])
    target = str(post['target'])

    # TODO: Need to handle name collisions 
    first = Character.objects.get(first_name__iexact=source)
    second = Character.objects.get(first_name__iexact=target)

    Relationship.objects.create(character_1=first, character_2=second)

    return HttpResponse('Success')

@csrf_exempt
def delete_relationship(request):
    post = request.POST

    c1 = Character.objects.get(first_name__iexact=post['source'])
    c2 = Character.objects.get(first_name__iexact=post['target'])

    try:
        r = Relationship.objects.get(character_1=c1, character_2=c2)
    except Relationship.DoesNotExist:
        try: 
            r= Relationship.object.get(character_1=c2, character_2=c2)
        except Relationship.DoesNotExist:
            return HttpResponse('DoesNotExist')

    if r:
        r.delete()
        return HttpResponse('Success')
    else:
        return HttpResponse('Failure')
