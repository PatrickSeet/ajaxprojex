from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from pokemon.forms import EmailUserCreationForm
from pokemon.models import Team
from pokemon.models import Pokemon
import json
from django.conf import settings

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            user.email_user("Welcome!", "Thank you for signing up for our website.")
            text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            html_content = '<h2>Thanks {} {}for signing up!</h2> <div>I hope you enjoy using our site</div><div>Signed up on {}'.format(user.first_name, user.last_name,user.date_joined)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("login")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required
def profile(request): ##return render(request, 'registration/profile.html')

    data = {
        'teams': Team.objects.filter(player_id=request.user.id)
    }
    return  render(request,'registration/profile.html', data)

@login_required
@csrf_exempt
def all_pokemon(request):

    pokemon = Pokemon.objects.all()
    data = serializers.serialize('json', pokemon)

    return HttpResponse(data, content_type='application/json')

@login_required
@csrf_exempt
def pokemon_data_dump(request):
    pokemon_objects = Pokemon.objects.all()
    collection = []
    for pokemon in pokemon_objects:
        collection.append({
            'name': pokemon.name,
            'image': pokemon.image,
            'pokedex_id': pokemon.pokedex_id,
            'team': {
                'id': pokemon.team.id,
                'name': pokemon.team.name
            }
        })
    return HttpResponse(
                json.dumps(collection),
                content_type='application.json'
           )

@login_required
@csrf_exempt
def new_pokemon(request):
    pokemon_list = []
    if request.method == 'POST':
        data = json.loads(request.body)
        teamname = data.pop()
        teamobjs = Team.objects.filter(name=teamname)
        team = teamobjs[:1][0]
        for item in data:
            pokemon = Pokemon.objects.create(name=item['name'][:-5], image=item['image'], pokedex_id=item['id'], team=team)
            pokemon_single = serializers.serialize('json',[pokemon])
            pokemon_list.append(pokemon_single)

    response = pokemon_list
    return HttpResponse(response, content_type='application/json')

@csrf_exempt
def new_team(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        team = Team.objects.create(name=data['name'], player=request.user)
        team_info = {'name': team.name}

        return HttpResponse(json.dumps(team_info), content_type='application/json')

@login_required
@csrf_exempt
def random(request):

    return render(request, 'random.html')

##
@login_required
@csrf_exempt
def view_team(request, team_id):

    pokemons = Pokemon.objects.filter(id=team_id)
    data = {'pokemons': pokemons}

    #imageURL = 'http://pokeapi.co'

    return render(request, 'view_team.html', data)

@login_required
@csrf_exempt
def pokemon_info(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=1)
    imageURL = 'http://pokeapi.co'
    this_pokemon = {
        'name': pokemon.name,
        'image': imageURL + pokemon.image,
        'pokedex_id': pokemon.pokedex_id,
        'team': {
            'id': pokemon.team.id,
            'name': pokemon.team.name
        }
    }
    return render_to_response('pokemon_info.html', this_pokemon)