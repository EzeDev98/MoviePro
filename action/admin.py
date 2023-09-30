from django.contrib import admin
from .models import Action
from django.utils.html import format_html

# Register your models here.
class ActionAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius: 1px;" />'.format(object.photo.url))
    
    thumbnail.short_description = 'photo'
    list_display = ('id', 'thumbnail', 'title', 'origin', 'genre', 'category', 'stars', 'writer', 'director', 'year')
    list_display_links = ('id', 'thumbnail', 'title', 'origin', 'genre', 'category', 'year')
    search_fields = ('title', 'origin', 'genre', 'category',  'year')
    list_filter = ('title', 'origin', 'genre', 'category',  'year')
    


admin.site.register(Action, ActionAdmin)
