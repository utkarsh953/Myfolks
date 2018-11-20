from django.conf.urls import url
from django.contrib import admin
from .views import (ProfileListAPIView,ProfileDetailsAPIView,ProfileCreateAPIView,ProfileUpdateAPIView,ProfileDeleteAPIView,
                    CategoryListAPIView,SubCategoryListAPIView)

urlpatterns = [
    url(r'^$', ProfileListAPIView.as_view(), name='list'),
    url(r'^create/$', ProfileCreateAPIView.as_view(),name='create'),
    url(r'^category/$', CategoryListAPIView.as_view(),name='category'),
    url(r'^category/(?P<pk>\d+)$', SubCategoryListAPIView.as_view(),name='subcategory'),
    url(r'^(?P<pk>\d+)/$', ProfileDetailsAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', ProfileUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', ProfileDeleteAPIView.as_view(), name='delete'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]
