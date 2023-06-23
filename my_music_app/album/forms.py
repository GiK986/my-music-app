from django import forms
from my_music_app.album.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Album Name'}
            ),
            'image_url': forms.TextInput(
                attrs={'placeholder': 'Image URL'}
            ),
            'genre': forms.Select(
                attrs={'placeholder': 'Genre'}
            ),
            'artist': forms.TextInput(
                attrs={'placeholder': 'Artist'}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': 'Price'}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Description'}
            ),
        }

        labels = {
            'name': 'Album Name:',
            'image_url': 'Image URL:',
            'genre': 'Genre:',
            'artist': 'Artist:',
            'price': 'Price:',
        }


class DeleteAlbumForm(AlbumForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'readonly': True}
            ),
            'image_url': forms.TextInput(
                attrs={'readonly': True}
            ),
            'genre': forms.TextInput(
                attrs={'readonly': True}
            ),
            'artist': forms.TextInput(
                attrs={'readonly': True}
            ),
            'price': forms.NumberInput(
                attrs={'readonly': True}
            ),
            'description': forms.Textarea(
                attrs={'readonly': True}
            ),
        }
