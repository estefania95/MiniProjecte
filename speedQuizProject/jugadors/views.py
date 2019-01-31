from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import JugadorForm, ExtendedUserCreationForm

# Create your views here.
def benvinguda(request):
    return render(request, 'benvinguda/index.html', {})

def botiga(request):
    return render(request, 'botiga/botiga.html', {})

def home(request):
  if request.user.is_authenticated:
    username = request.user.username
  else:
    username = 'no tas logejat'

  context = {'username' : username}
  return render(request, 'home/home.html', context)

def iniciSessio(request):
    return render(request, 'registration/login.html', {})

def joc(request):
    return render(request, 'joc/unJugador.html', {})

def puntuacio(request):
    return render(request, 'puntuacio/puntuacio.html', {})

def registre(request):
    return render(request, 'registre/registrarse.html', {})
