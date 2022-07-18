from django.contrib import admin
from .models import Movie, MovieInstance, Director, Genero

# Register your models here.

admin.site.register(Director)
admin.site.register(Genero)
admin.site.register(Movie)
admin.site.register(MovieInstance)
