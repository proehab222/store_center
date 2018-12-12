from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from electronic.views import  category
urlpatterns = [
    path('category/',category.listCategory ,name="listing"),
    url(r'^category/(?P<cat_id>\d+)/$',category.getCategory),
    url(r'^category/(?P<cat_id>\d+)/delete/$',category.ondelete)
]
