from django.urls import path
from . import views

urlpatterns = [
    path('', views.series, name='series'),
    path('<int:id>', views.single_series, name='single_series'),
]