from rest_framework import viewsets
from .serializers import BlogSerializer
from .models import Blog
import random

class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.order_by('?')
    serializer_class = BlogSerializer
    filter_fields = ['topic__topic']
    search_fields = ['title', 'topic__topic']
