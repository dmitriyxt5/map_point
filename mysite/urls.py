from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Этот код заставит Django отдавать медиа и локально, и на сервере при DEBUG=False
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

urlpatterns += [
    path('', include('map_points.urls')),
    path('map/', include('map_points.urls')),
]