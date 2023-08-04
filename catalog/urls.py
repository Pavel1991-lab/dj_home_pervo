from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from catalog.views import Contactlistview, ProductByCategoryListView, Productlistview, Productcreateview



urlpatterns = [
    path('', Productlistview.as_view(), name='product_list'),
    path('contacts/', Contactlistview.as_view(), name = 'contact_list'),
    path('good/<int:pk>', ProductByCategoryListView.as_view(), name='product_detail'),
    path('blog/', Productcreateview.as_view(), name = 'blog_list'),
    path('create/', Productcreateview.as_view(), name='create'),
    # path('', ..., name='list'),
    # path('view/<int:pk>/', ..., name='view'),
    # path('edit/<int:pk>/', ..., name='edit'),
    # path('delete/<int:pk>/', ..., name='delete')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


