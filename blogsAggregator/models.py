from django.db import models
from topics.models import Topic


class RSSLink(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    owner = models.CharField(max_length=50)
    link = models.URLField()

    class Meta:
        unique_together = ['topic', 'owner', 'link']


class Blog(models.Model):
    topic = models.ForeignKey(
        Topic, related_name='blogaggregator_set', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    cover_image = models.URLField(null=True, blank=True)
    summary = models.TextField(max_length=500)
    link = models.URLField()
    uploaded_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['topic', 'link']