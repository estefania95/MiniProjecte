from django.shortcuts import render

# Create your views here.
def benvinguda(request):
    return render(request, 'benvinguda/index.html', {})
