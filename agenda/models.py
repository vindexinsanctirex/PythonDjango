from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=144)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_at = timezone.now()
        self.save()
        
