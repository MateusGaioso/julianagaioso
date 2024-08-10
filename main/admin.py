from django.contrib import admin
from .models import Video
from simple_history.admin import SimpleHistoryAdmin

 
@admin.register(Video)
class VideoAdmin(SimpleHistoryAdmin):
    list_display = ('nome', 'video', 'active', 'created_at', 'modified_at')
    search_fields = ('nome',)
    list_filter = ('nome', 'active')
    ordering = ('nome',)
    date_hierarchy = 'created_at'