from django.db import models


class Topic(models.Model):
    topic = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.topic
