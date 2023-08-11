from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from fidbeck.apps import FidbeckConfig

from fidbeck.views import Fidbeckcreateview, FidbecklistView, Fidbecdetaileview, Fidbecupdateview, FidbecdeleteView



app_name = FidbeckConfig.name



urlpatterns = [
    path('create/', Fidbeckcreateview.as_view(), name='create'),
    path('', FidbecklistView.as_view(), name='list'),
    path('view/<slug:slug>', Fidbecdetaileview.as_view(), name='view'),
    path('edit/<slug:slug>', Fidbecupdateview.as_view(), name='edit'),
    path('delete/<slug:slug>', FidbecdeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


