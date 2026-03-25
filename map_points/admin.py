from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import MapPoint 

# 1. Переопределяем User (только один раз во всем проекте!)
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

@admin.register(User)
class DemoUserAdmin(UserAdmin):
    def has_delete_permission(self, request, obj=None):
        return False if request.user.username == "demo" else super().has_delete_permission(request, obj)
    def has_add_permission(self, request):
        return False if request.user.username == "demo" else super().has_add_permission(request)

# 2. Регистрируем MapPoint (только один раз во всем проекте!)
@admin.register(MapPoint)
class MapPointAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at')
    
    def has_module_permission(self, request):
        return True # Чтобы demo видел блок в меню

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if request.user.username == "demo":
            return True
        return super().has_change_permission(request, obj)

    def has_add_permission(self, request):
        if request.user.username == "demo":
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if request.user.username == "demo":
            return False
        return super().has_delete_permission(request, obj)