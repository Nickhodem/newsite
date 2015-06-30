from django.conf.urls import patterns, url
from scanning import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^scanners/', views.scanners, name='scanners'),)
