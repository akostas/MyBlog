from django.contrib import admin
from .models import BlogPost
# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title', 'content']
    autocomplete_fields = ['author']



admin.site.register(BlogPost, BlogPostAdmin)