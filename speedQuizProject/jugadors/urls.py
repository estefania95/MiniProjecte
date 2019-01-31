from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.benvinguda, name='benvinguda'),
    path('registre/', views.registre, name='registre'),
    path('iniciSessio/', views.iniciSessio, name='iniciSessio'),
    path('home/', include([
        path('', views.home, name='home'),
        path('botiga/', views.botiga, name='botiga'),
        path('joc/', views.joc, name='joc'),
        path('puntuacio/', views.puntuacio, name='puntuacio'),
    ])),
]