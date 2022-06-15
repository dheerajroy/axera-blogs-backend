from rest_framework import viewsets
from .serializers import TopicSerializer
from .models import Topic

class TopicViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.all().order_by('id')
    serializer_class = TopicSerializer
    filter_fields = search_fields = ['topic__topic']

    def paginate_queryset(self, queryset, view=None):
        return None