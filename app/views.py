from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from .forms import SongCreateForm, AddYoutubeForm, AddPersonForm, AddArtistForm
from .models import Song, Youtube, Person, Artist


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
    return render(request, 'app/form.html', context)


def add_youtube(request, id):
    form = AddYoutubeForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        if is_youtube_url(request.POST['url']):
            youtube = form.save(commit = False)
            youtube.song = Song.objects.get(id=id)
            youtube.save()
            return redirect('app:index')

    context = {
        'form': AddYoutubeForm(),
        'song': Song.objects.get(id=id),
#        'song_id': request.GET['song_id'],
    }
    return render(request, 'app/form.html', context)


'''引数として受け取ったURLがYoutube動画のものかチェックする関数'''
def is_youtube_url(url):
    if url[:23] == 'https://www.youtube.com':
        return True
    elif url[:16] == 'https://youtu.be':
        return True
    else:
        return False


def detail(request, id):
    song = get_object_or_404(Song, id=id)

    context = {
        'song': song,
    }
    return render(request, 'app/song_detail.html', context)


def add_person(request):
    form = AddPersonForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('app:index')

    context = {
        'form': AddPersonForm()
    }
    return render(request, 'app/form.html', context)


def add_artist(request):
    form = AddArtistForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('app:index')

    context = {
        'form': AddArtistForm()
    }
    return render(request, 'app/form.html', context)
