from django.shortcuts import render, redirect
from my_music_app.user_profile.models import Profile
from my_music_app.user_profile.forms import ProfileForm
from my_music_app.album.models import Album


# Create your views here.
def index(request):
    profile = Profile.objects.first()
    form = ProfileForm()
    albums = Album.objects.all()

    context = {
        'profile': profile,
        'form': form,
        'albums': albums,
    }

    if profile:
        return render(request, 'common/home-with-profile.html', context=context)

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('home page')

    return render(request, 'common/home-no-profile.html', context=context)
