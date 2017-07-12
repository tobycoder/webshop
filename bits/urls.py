from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from django.conf import settings
admin.autodiscover()
app_name = 'bits'
urlpatterns = [
    url(r'^$', views.get_index, name='get_index'),
    url(r'^shop/(?P<shop_item>[^/?]+)/$', views.get_product, name='get_product'),
    url(r'^shop/(?P<shop_item>[^/?]+)/(?P<shop_subitem>[^/?]+)/$', views.get_product_by_sub, name='get_product_by_sub'),
    url(r'^product/(?P<product_item>[^/?]+)/$', views.get_product_solo, name='get_product_solo'),
    url(r'^(?P<shop_item>[^/?]+)/new/$', views.get_product_by_new, name='get_product_by_new'),
    url(r'^new/$', views.get_product_by_new_solo, name='get_product_by_new'),
    url(r'^contact/$', views.contact_request, name='contact'),
    url(r'^cart/$', views.view_cart, name='view_cart'),
    url(r'^cart/add-to-cart/$', views.add_to_cart, name='add_to_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)