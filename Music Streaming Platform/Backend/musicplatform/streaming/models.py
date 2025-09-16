from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='music/')
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Create your models here.
