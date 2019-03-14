from django.conf.urls import url
from .import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^iniciarsesion/$', views.iniciarsesion),
    url(r'^administracion/$', views.administracion),
    url(r'^administracion/eliminar/(?P<pk>[0-9]+)$', views.administracion_eliminar),
    url(r'^administracion/editar/(?P<pk>[0-9]+)$', views.administracion_editar),
    url(r'^administracion/nuevo/', views.administracion_nuevo),
    url(r'^cliente/eliminar/(?P<pk>[0-9]+)$', views.cliente_eliminar),
    url(r'^cliente/editar/(?P<pk>[0-9]+)$', views.cliente_editar),
    url(r'^cliente/nuevo/', views.cliente_nuevo),
    url(r'^clientes/$', views.clientes),
    url(r'^orden/(?P<pk>[0-9]+)$$', views.orden),
    url(r'getdata',views.getdata),
]



