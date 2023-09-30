from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Adventure

# Create your views here.
@login_required(login_url = 'login')
def adventure(request):
    adventure_movies = Adventure.objects.order_by('-created_date')
    data = {
        'adventure_movies': adventure_movies,
    }
    return render(request, 'adventure/adventure.html', data)


def single_adventure(request, id):
    single_adventure = get_object_or_404(Adventure, pk=id)
    data = {
        'single_adventure': single_adventure,
    }
    return render(request, 'adventure/movie.html', data)