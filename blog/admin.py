from django.contrib import admin
from blog.models import *

class BlogCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogCategory, BlogCategoryAdmin)


class BlogTopicAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'category', 'status')
    list_filter = ('category',)
    search_fields = ['title']
    list_editable = [ 'status' ]

admin.site.register(BlogTopic, BlogTopicAdmin)
