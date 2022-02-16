from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from .forms import SongCreateForm, AddYoutubeForm
from .models import Song, Youtube


def index(request):
    context = {
        'song_list': Song.objects.all(),
    }
    return render(request, 'app/top.html', context)


def add(request):
    form = SongCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('app:index')

    context = {
        'form': SongCreateForm()
    }
    return render(request, 'app/song_form.html', context)


def add_youtube(request):
    form = AddYoutubeForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        youtube = form.save(commit = False)
        youtube.song = request.GET['song_name']
        return redirect('app:index')

    context = {
        'form': AddYoutubeForm(),
        'song_name': request.GET['song_name'],
    }
    return render(request, 'app/youtube_form.html', context)


def detail(request, pk):
    song = get_object_or_404(Song, pk=pk)

    context = {
        'song': song,
    }
    return render(request, 'app/song_detail.html', context)