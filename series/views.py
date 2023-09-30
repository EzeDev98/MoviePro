from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Serie

# Create your views here.
@login_required(login_url = 'login')
def series(request):
    series_movies = Serie.objects.order_by('-created_date')
    data = {
        'series_movies': series_movies,
    }
    return render(request, 'series/series.html', data)

def single_series(request, id):
    single_series = get_object_or_404(Serie, pk=id)
    data = {
        'single_series': single_series,
    }
    return render(request, 'series/movie.html', data)