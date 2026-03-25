from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import MapPoint

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

class DemoPermissionMixin:
    """
    Миксин для ограничения прав пользователя 'demo'.
    """
    def has_delete_permission(self, request, obj=None):
        if request.user.username == "demo":
            return False
        return super().has_delete_permission(request, obj)

    def has_add_permission(self, request):
        if request.user.username == "demo":
            return False
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if request.user.username == "demo":
            return True
        return super().has_change_permission(request, obj)

@admin.register(User)
class DemoUserAdmin(DemoPermissionMixin, UserAdmin):
    pass

@admin.register(MapPoint)
class DemoAdmin(DemoPermissionMixin, admin.ModelAdmin):
    list_display = ['__str__']