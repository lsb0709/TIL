from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    return render(request, 'movies/main.html')

def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movies:index')
    else:
        movie_form = MovieForm()
    context = {
        'movie_form': movie_form,
    }
    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie,
    }
    return render(request, 'movies/detail.html', context)



@login_required
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie_form = MovieForm(instance=movie)

    if request.method == 'POST':
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movies:detail', movie.pk)
        else:
            movie_form = MovieForm(instance=movie)
    context = {
        'movie_form':movie_form,
    }
    return render(request, 'movies/update.html', context)

@login_required
def delete(request, pk):
    Movie.objects.get(pk=pk).delete()
    return redirect('movies:index')