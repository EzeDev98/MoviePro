from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Action

# Create your views here.
@login_required(login_url = 'login')
def action(request):
    action_movies = Action.objects.order_by('-created_date')
    data = {
        'action_movies': action_movies,
    }
    return render(request, 'action/action.html', data)

def single_action(request, id):
    single_action = get_object_or_404(Action, pk=id)
        
    data = {
        'single_action': single_action,
    }
    return render(request, 'action/movie.html', data)
