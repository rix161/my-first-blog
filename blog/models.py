from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 180)
    text = models.TextField()
    pub_Date = models.DateTimeField(blank=True,null=True)
    created_Date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.pub_Date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


