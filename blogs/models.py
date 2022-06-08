from django.db import models
from django.contrib.auth.models import User
from topics.models import Topic

class Blog(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='cover_images',null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    written_by = models.ForeignKey(User, on_delete=models.CASCADE)
    published_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.topic}: {self.title}'
