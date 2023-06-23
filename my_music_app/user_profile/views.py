from django.shortcuts import render, redirect

from my_music_app.user_profile.models import Profile
from my_music_app.album.models import Album


# Create your views here.
def details(request):
    profile = Profile.objects.first()
    albums_count = Album.objects.count()
    context = {
        'profile': profile,
        'albums_count': albums_count,
    }
    return render(request, 'user_profile/profile-details.html', context=context)


def delete(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile = Profile.objects.first()
        profile.delete()
        return redirect('home page')

    context = {
        'profile': profile,
    }
    return render(request, 'user_profile/profile-delete.html', context=context)
