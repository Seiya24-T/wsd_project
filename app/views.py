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


def add_youtube(request, id):
    form = AddYoutubeForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        youtube = form.save(commit = False)
        youtube.song = Song.objects.get(id=id)
        youtube.save()
        return redirect('app:index')

    context = {
        'form': AddYoutubeForm(),
        'song': Song.objects.get(id=id),
#        'song_id': request.GET['song_id'],
    }
    return render(request, 'app/youtube_form.html', context)


def detail(request, id):
    song = get_object_or_404(Song, id=id)

    context = {
        'song': song,
    }
    return render(request, 'app/song_detail.html', context)
