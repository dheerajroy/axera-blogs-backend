from django.contrib import admin
from .models import RSSLink, Blog

@admin.register(RSSLink)
class RSSLinkAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'topic__topic', 'link']
    list_display = ['topic', 'owner', 'link']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    search_fields = ['topic__topic', 'title']
    list_display = ['topic', 'title', 'uploaded_datetime']
    list_filter = ['topic']
