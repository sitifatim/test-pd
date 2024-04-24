from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Movie

def movies(request):
    movies = Movie.objects.all().order_by('-userRating')
    return render(request, 'movies/movies.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/movie_details.html', {'movie': movie})

