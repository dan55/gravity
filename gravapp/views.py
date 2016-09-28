from django.http import HttpResponse
from django.shortcuts import render

from gravapp.models import Character, Relationship
from .forms import CharacterForm

from django.views.decorators.csrf import csrf_exempt

def index(request):
    characters = Character.objects.all()
    relationships = Relationship.objects.all()

    nodes, links, graph = [], [], {}

    for character in characters:
        name = str(character)
        nodes.append({ 'name': name, 'group': 0 })
        graph[name] = []

    for rel in relationships:
        source = str(rel.character_1)
        target = str(rel.character_2)

        links.append({ 'source': source, 'target': target })

        graph[source].append(target)
        graph[target].append(source)
    #links.append({ 'source': 0, 'target': 1 })

    update_character_groups(nodes, graph)

    context = { 'nodes': nodes, 'links': links, 'graph': graph }
    form = CharacterForm()

    return render(request, 'index.html', { 'context': context, 'form': form })

def dfs(start, graph, visited=None):
    if visited is None:
        visited = [start]

    for node in graph[start]:
        if node not in visited:
            visited.append(node)
            dfs(node, graph, visited)

    return visited

def update_group(nodes, visited, group_num):
    for character in visited:
        for node in nodes:
            if character == node['name']:
                node['group'] = group_num

def update_character_groups(nodes, graph):
    '''
    Takes a set of characters (node's name) and groups them into connected components (node's group)
    '''
    connected_components = 1

    for node in nodes:
        if node['group'] == 0: # has not been visited
            update_group(nodes, dfs(node['name'], graph), connected_components)
            connected_components += 1

    return nodes

def get_first_name(full_name): 
    return full_name.split()[0]

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

    Character.objects.filter(first_name__iexact=get_first_name(request.POST['name'])).delete()

    return HttpResponse('Success')

@csrf_exempt
def create_relationship(request):
    post = request.POST
    source = str(post['source'])
    target = str(post['target'])
    page_num = post['page_num']

    # TODO: Need to handle name collisions / change to full names 
    first = Character.objects.get(first_name__iexact=get_first_name(source))
    second = Character.objects.get(first_name__iexact=get_first_name(target))

    Relationship.objects.create(character_1=first, character_2=second, page=page_num)

    return HttpResponse('Success')

@csrf_exempt
def delete_relationship(request):
    post = request.POST

    c1 = Character.objects.get(first_name__iexact=get_first_name(post['source']))
    c2 = Character.objects.get(first_name__iexact=get_first_name(post['target']))

    try:
        r = Relationship.objects.get(character_1=c1, character_2=c2)
    except Relationship.DoesNotExist:
        try: 
            r= Relationship.objects.get(character_1=c2, character_2=c1)
        except Relationship.DoesNotExist:
            return HttpResponse('DoesNotExist')

    if r:
        r.delete()
        return HttpResponse('Success')
    else:
        return HttpResponse('Failure')
