"""Posts admin classes"""
# Django
from django.contrib import admin

# Models
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('user', 'title', 'photo')
    list_display_links = ('user',)
    list_editable = ('title','photo')
    search_fields = ('user', 'title', 'created', 'modified')
    list_filter = (
        'created',
        'modified'
    )


