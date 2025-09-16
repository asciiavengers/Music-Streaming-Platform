from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, SongForm
from .models import Song

def signup_view(request):
    form=CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.uploaded_by = request.user
            song.save()
            return redirect('home')
    else:
        form=SongForm()
    return render(request,'upload.html',{'form': form})
def home(request):
    songs = Song.objects.all()
    return render(request,'home.html',{'songs': songs})


# Create your views here.
