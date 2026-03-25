from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import MapPoint

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

class DemoUserAdmin(UserAdmin):
    def has_delete_permission(self, request, obj=None):
        return False if request.user.username == "demo" else super().has_delete_permission(request, obj)
    def has_add_permission(self, request):
        return False if request.user.username == "demo" else super().has_add_permission(request, obj)
    def has_change_permission(self, request, obj=None):
        return True if request.user.username == "demo" else super().has_change_permission(request, obj)

admin.site.register(User, DemoUserAdmin)

class DemoAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False if request.user.username == "demo" else super().has_delete_permission(request, obj)
    def has_add_permission(self, request):
        return False if request.user.username == "demo" else super().has_add_permission(request, obj)
    def has_change_permission(self, request, obj=None):
        return True if request.user.username == "demo" else super().has_change_permission(request, obj)

admin.site.register(MapPoint, DemoAdmin)
