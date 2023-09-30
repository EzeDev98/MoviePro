from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_movies', views.all_movies, name='all_movies'),
    path('<int:id>', views.single_movies, name='single_movies'),
    path('search', views.search, name='search'),
    path('<int:id>', views.single_search, name='single_search'),
]