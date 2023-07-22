from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from catalog.views import home, contacts

urlpatterns = [
    path('', home),
    path('contacts/', contacts)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
