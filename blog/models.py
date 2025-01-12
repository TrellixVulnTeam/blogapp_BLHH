from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length = 100)
    Content = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User,on_delete= models.CASCADE)

    def __str__(self):
        return self.Title