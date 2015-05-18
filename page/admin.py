from django.contrib import admin
from page.models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ("title","content")

admin.site.register(Page, PageAdmin)
