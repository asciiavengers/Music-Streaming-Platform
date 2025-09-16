from django import forms
from .models import Song
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields = UserCreationForm.Meta.fields + ('email',)

class SongForm(forms.ModelForm):
    class Meta:
        model=Song
        fields=['title','artist','audio_file']
