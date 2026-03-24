from django.contrib import admin
from .models import MapPoint


@admin.register(MapPoint)
class MapPointAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'status',
        'latitude',
        'longitude',
        'created_at',
    )

    list_filter = ('status',)
    search_fields = ('title', 'description')
    list_editable = ('status',)
