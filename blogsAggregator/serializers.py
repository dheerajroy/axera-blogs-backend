from .models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['__all__']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['topic'] = instance.topic.topic
    
        return response
