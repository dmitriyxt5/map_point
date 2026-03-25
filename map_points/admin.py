from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass 

class DemoUserAdmin(UserAdmin):
    def has_delete_permission(self, request, obj=None):
        if request.user.username == "demo":
            return False
        return super().has_delete_permission(request, obj)

    def has_add_permission(self, request):
        if request.user.username == "demo":
            return False
        return super().has_add_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        if request.user.username == "demo":
            return True
        return super().has_change_permission(request, obj)

admin.site.register(User, DemoUserAdmin)
