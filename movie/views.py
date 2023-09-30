from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Movie

# Create your views here.
def home(request):
    return render(request, 'movies/home.html')

@login_required(login_url = 'login')
def all_movies(request):
    all_movies = Movie.objects.order_by('-created_date')
    data = {
        'all_movies': all_movies,
    }
    return render(request, 'movies/all_movie.html', data)

def single_movies(request, id):
    
    single_movie = get_object_or_404(Movie, pk=id)
    data = {
        'single_movie': single_movie,
    }
    return render(request, 'movies/movie.html', data)

@login_required(login_url = 'login')
def search(request):
    search_movies = Movie.objects.order_by('-created_date')
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            search_movies = search_movies.filter(title__icontains=keyword)
            
    data = {
        'search_movies': search_movies,
    }
    return render(request, 'search/search.html', data)

def single_search(request, id):
    
    single_search = get_object_or_404(Movie, pk=id)
    data = {
        'single_search': single_search,
    }
    return render(request, 'search/movie.html', data)

