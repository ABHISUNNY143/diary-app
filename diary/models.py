from django.db import models
from django.contrib.auth.models import User
import os

def diary_upload_path(instance, filename):
    title = instance.diary.title.replace(" ", "_")
    return f"diaries/{title}/{filename}"

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class DiaryFile(models.Model):
    diary = models.ForeignKey(Diary, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to=diary_upload_path)
