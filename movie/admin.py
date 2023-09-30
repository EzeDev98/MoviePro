from django.contrib import admin
from .models import Movie
from django.utils.html import format_html

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius: 1px;" />'.format(object.photo.url))
    
    thumbnail.short_description = 'photo'
    list_display = ('id', 'thumbnail', 'title', 'origin', 'genre', 'category_1', 'stars', 'writer', 'director', 'year')
    list_display_links = ('id', 'thumbnail', 'title', 'origin', 'genre', 'category_1', 'year')
    search_fields = ('title', 'origin', 'genre', 'category_1',  'year')
    list_filter = ('title', 'category_1', 'origin', 'genre',  'year')
    


admin.site.register(Movie, MovieAdmin)
