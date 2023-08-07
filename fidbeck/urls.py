from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from fidbeck.apps import FidbeckConfig

from fidbeck.views import Fidbeckcreateview

app_name = FidbeckConfig.name



urlpatterns = [
    path('create/', Fidbeckcreateview.as_view(), name='create'),
    # path('', ..., name='list'),
    # path('view/<int:pk>', ..., name='view'),
]


