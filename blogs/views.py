from rest_framework import viewsets
from blogs.serializers import BlogSerializer
from blogs.models import Blog


class BlogViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer
    filter_fields = ['topic__topic']
    search_fields = ['title', 'topic__topic']
