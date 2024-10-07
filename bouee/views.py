from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Bouee, DonneesGnss, DonneesCapteures
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import json

def welcome(request):
    return render(request, 'alltem/welcome.html')

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('signin')
        else:
           messages.error(request, 'An error occurred during registration')
    return render(request, 'alltem/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')
    return render(request, 'alltem/signin.html')

def logoutuser(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def home(request):
    Bouees = Bouee.objects.all()
    return render(request, 'alltem/home.html', {'Bouees':Bouees})

@login_required(login_url='signin')
def affiche(request):
    if request.method == 'POST':
        s = request.POST.get('Bouee')
    bouee_selected=Bouee.objects.get(name=s)
    DonneeGnss = DonneesGnss.objects.filter(bouee=bouee_selected)
    context={'DonneeGnss':DonneeGnss, 'bouee_selected':bouee_selected}
    return render(request, 'alltem/affiche.html', context)

@login_required(login_url='signin')
def affichetemp(request):
    q=request.GET.get('q')
    bouee_selected=Bouee.objects.get(id=q)
    DonneesCapt = DonneesCapteures.objects.filter(bouee=bouee_selected)
    # Récupérer les données de température et de date
    temperatures = [donnees.temp for donnees in DonneesCapt]
    dates = [donnees.date for donnees in DonneesCapt]

    # Convertir les données en JSON pour les transmettre au template
    data_json = json.dumps({'dates': dates, 'temperatures': temperatures})

    return render(request, 'alltem/affichetemp.html', {'data_json': data_json})

    

@login_required(login_url='signin')
def affichepress(request):
    q=request.GET.get('q')
    bouee_selected=Bouee.objects.get(id=q)
    DonneesCapt = DonneesCapteures.objects.filter(bouee=bouee_selected)
    # Récupérer les données de température et de date
    pressions = [donnees.press for donnees in DonneesCapt]
    dates = [donnees.date for donnees in DonneesCapt]

    # Convertir les données en JSON pour les transmettre au template
    data_json = json.dumps({'dates': dates, 'pressions': pressions})

    return render(request, 'alltem/affichepress.html', {'data_json': data_json})


@login_required(login_url='signin')
def affichehum(request):
    q=request.GET.get('q')
    bouee_selected=Bouee.objects.get(id=q)
    DonneesCapt = DonneesCapteures.objects.filter(bouee=bouee_selected)
    # Récupérer les données de température et de date
    humidites = [donnees.hum for donnees in DonneesCapt]
    dates = [donnees.date for donnees in DonneesCapt]

    # Convertir les données en JSON pour les transmettre au template
    data_json = json.dumps({'dates': dates, 'humidites': humidites})

    return render(request, 'alltem/affichehum.html', {'data_json': data_json})

@login_required(login_url='signin')
def affichemap(request):
    q = request.GET.get('q')
    bouee_selected=Bouee.objects.get(id=q)
    DonneeGnss = DonneesGnss.objects.filter(bouee=bouee_selected)
    context={'DonneeGnss':DonneeGnss, 'bouee_selected':bouee_selected}
    return render(request, 'alltem/map.html', context)