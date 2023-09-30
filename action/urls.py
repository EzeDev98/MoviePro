from django.urls import path
from . import views

urlpatterns = [
    path('', views.action, name='action'),
    path('<int:id>', views.single_action, name='single_action'),
]