from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from electronic.views import  category
urlpatterns = [
    path('category/',category.listCategory ),
    url(r'^category/(?P<cat_id>\d+)/$',category.getCategory)
]
