from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('catalog.urls', namespace='catalog')),
    path('admin/', admin.site.urls),
    path('fidbeck/', include('fidbeck.urls', namespace='fidbeck')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
