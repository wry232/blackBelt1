from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^item/(?P<id>\d+)$', views.item, name='item'),
    url(r'^create$', views.create, name='create'),
    url(r'^add$', views.add, name='add'),
     url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^additem/(?P<id>\d+)$', views.additem, name='additem'),
    url(r'^removeitem/(?P<id>\d+)$', views.removeitem, name='removeitem'),
    # url(r'^product/(?P<id>\d+)$', views.product, name='product'),
]

