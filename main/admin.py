from django.contrib import admin
from .models import Point 

class PointAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Point, PointAdmin)
