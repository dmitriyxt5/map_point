from django.contrib import admin

# Register your models here.
class PointAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
