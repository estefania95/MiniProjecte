from django.shortcuts import render

# Create your views here.
def benvinguda(request):
    return render(request, 'benvinguda/index.html', {})

def botiga(request):
    return render(request, 'botiga/botiga.html', {})

def home(request):
    return render(request, 'home/home.html', {})

def iniciSessio(request):
    return render(request, 'iniciarSessio/iniciarSessio.html', {})

def joc(request):
    return render(request, 'joc/unJugador.html', {})

def puntuacio(request):
    return render(request, 'puntuacio/puntuacio.html', {})

def registre(request):
    return render(request, 'registre/registrarse.html', {})