from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from catalog.views import Contactlistview, ProductDetailView, Productlistview

urlpatterns = [
    path('', Productlistview.as_view(), name='product_list'),
    path('contacts/', Contactlistview.as_view(), name = 'contact_list'),
    path('good/<int:pk>', ProductDetailView.as_view(), name='product_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


