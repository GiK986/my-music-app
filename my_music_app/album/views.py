from django.shortcuts import render, redirect
from my_music_app.album.models import Album
from my_music_app.album.forms import AlbumForm, DeleteAlbumForm
from my_music_app.user_profile.models import Profile


# Create your views here.
def add(request):
    profile = Profile.objects.first()
    form = AlbumForm()

    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'album/add-album.html', context=context)


def details(request, pk):
    album = Album.objects.get(pk=pk)
    profile = Profile.objects.first()

    context = {
        'album': album,
        'profile': profile,
    }
    return render(request, 'album/album-details.html', context=context)


def edit(request, pk):
    album = Album.objects.get(pk=pk)
    profile = Profile.objects.first()
    form = AlbumForm(instance=album)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'album': album,
        'profile': profile,
        'form': form,
    }

    return render(request, 'album/edit-album.html', context=context)


def delete(request, pk):
    album = Album.objects.get(pk=pk)
    profile = Profile.objects.first()
    form = DeleteAlbumForm(instance=album)

    if request.method == 'POST':
        album.delete()
        return redirect('home page')

    context = {
        'album': album,
        'profile': profile,
        'form': form,
    }

    return render(request, 'album/delete-album.html', context=context)
