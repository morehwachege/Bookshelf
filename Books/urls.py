from django.urls import path
from .views import home, fantasy, politics

urlpatterns = [
    path('', home, name='home'),
    path('fantasy/', fantasy, name='fantasy_books'),
    path('politics/', politics, name='politics_books')
]