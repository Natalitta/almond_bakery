from django.contrib import admin
from .models import MenuItem
from django_summernote.admin import SummernoteModelAdmin


@admin.register(MenuItem)
class MenuItemAdmin(SummernoteModelAdmin):

    list_display = ('title', 'vegan')
    search_fields = ['title', 'content']
    list_filter = ('vegan',)
    summernote_fields = ('content',)
