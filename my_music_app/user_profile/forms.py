from django import forms
from my_music_app.user_profile.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Username'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email'}
            ),
            'age': forms.NumberInput(
                attrs={'placeholder': 'Age'}
            ),
        }

        labels = {
            'username': 'Username:',
            'email': 'Email:',
            'age': 'Age:',
        }