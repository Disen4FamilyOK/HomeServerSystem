from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings

urlpatterns = [
    path(r'jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
