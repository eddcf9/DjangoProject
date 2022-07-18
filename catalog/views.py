from dis import dis
from django.shortcuts import render
from .models import Movie, MovieInstance, Director, Genero

# Create your views here.
def index(request):
    num_movies = Movie.objects.all().count()
    movie_instances = MovieInstance.objects.all().count()
    num_Directors = Director.objects.all().count()

    disponibles = MovieInstance.objects.filter(status__exact = 'a').count()


    return render(
        request,
        'index.html',
        context={
            'num_movies': num_movies,
            'movie_instances': movie_instances,
            'num_Directors': num_Directors,
            'disponibles': disponibles
        }
    )

