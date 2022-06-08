from django.contrib import admin
from blogs.models import Blog

admin.site.site_header = 'Axera Blogs Panel'

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ['topic','cover_image', 'title', 'content', 'written_by']
    list_display = ['topic', 'title', 'written_by', 'published_datetime', 'updated_datetime']
    search_fields = ['title', 'content']
    list_filter = ['topic', 'written_by']
    
    def get_form(self, request, obj=None, **kwargs):
        if obj is None and not request.user.is_superuser:
            self.readonly_fields = ['written_by']
        elif obj is not None and not request.user.is_superuser:
            if obj.written_by == request.user:
                self.readonly_fields = ['written_by']
            else:
                self.readonly_fields = self.fields
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.written_by = request.user
            obj.save()
        else:
            return super().save_model(request, obj, form, change)
