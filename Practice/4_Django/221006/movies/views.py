from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
# 1. 게시글 목록
def index(request):
    movies = Movie.objects.all().order_by('-updated_at')
    context = {
        'movies': movies,
    }

    return render(request, 'movies/index.html', context)


# 2. 글 새로 생성
def create(request):
    form = MovieForm(request.POST or None)

    if form.is_valid():
        new_movie = form.save()
        # new_movie.summary = new_movie.summary.replace('\r\n', '<br>')
        # new_movie.save()

        return redirect('movies:detail', new_movie.pk)

    context = {
        'form': form,
    }

    return render(request, 'movies/create.html', context)


# 3. 글 세부 페이지
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }

    return render(request, 'movies/detail.html', context)


# 4. 글 수정
def update(request, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)

        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)

    else:
        form = MovieForm(instance=movie)

    context = {
        'movie': movie,
        'form': form,
    }

    return render(request, 'movies/update.html', context)


# 5. 글 삭제
def delete(request, pk):
    Movie.objects.get(pk=pk).delete()

    return redirect('movies:index')