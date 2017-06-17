from django.conf.urls import url, include
from django.contrib import admin
from . import views

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
]
