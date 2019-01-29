from django.urls import path
from . import views

urlpatterns = [
    path('', views.benvinguda, name='benvinguda'),
    path('botiga/', views.botiga, name='botiga'),
    path('home/', views.home, name='home'),
    path('iniciSessio/', views.iniciSessio, name='iniciSessio'),
    path('joc/', views.joc, name='joc'),
    path('puntuacio/', views.puntuacio, name='puntuacio'),
    path('registre/', views.registre, name='registre'),
]