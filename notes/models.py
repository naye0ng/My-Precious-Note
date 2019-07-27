from django.db import models
from django.conf import settings

# Create your models here.
class Note(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    isPublic = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # like_users : Note를 좋아하는 Users 조회
    # like_notes : User가 좋아하는 Notes 조회
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_notes', blank=True)
