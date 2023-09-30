from django.urls import path
from . import views

urlpatterns = [
    path('', views.adventure, name='adventure'),
    path('<int:id>', views.single_adventure, name='single_adventure'),
]