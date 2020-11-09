from django.contrib import admin

# Register your models here.
from .models import Post

from django.utils.html import strip_tags

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_num', 'post_title', 'post_content', 'post_date']
    list_display_links = ['post_num', 'post_title']

    def post_title(self):
        return strip_tags(self.post_title)

    search_fields = ['post_title']
    fields = ['post_title', 'post_content']


    