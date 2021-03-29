from django.urls import path
from .views import home, fantasy, politics, thriller, mystery,children, humour, pirate,ghost, havard,health, african, adventure

urlpatterns = [
    path('', home, name='home'),
    path('fantasy/', fantasy, name='fantasy_books'),
    path('politics/', politics, name='politics_books'),
    path('thriller/', thriller, name='thriller_books'),
    path('mystery/', mystery, name='mystery_books'),
    path('children/', children, name='children_books'),
    path('humour/', humour, name='humour_books'),
    path('pirate/', pirate, name='pirate_books'),
    path('ghost/', ghost, name='ghost_books'),
    path('havard/', havard, name='havard_books'),
    path('health/', health, name='health_books'),
    path('african/', african, name='african_books'),
    path('adventure/', adventure, name='adventure_books'),

]