from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from electronic.views import  category,product


app_name='elect_ehab'
urlpatterns = [
    path('category/',category.listCategory ,name="listing"),
    path('product/', product.listProduct, name="listing_Product"),

#path('category/add',TemplateView.as_view(template_name='add.html'),name="addCat"),
    path('category/add',category.addCategory,name="addCat"),
    url(r'^category/(?P<cat_id>\d+)/update/$',category.updateCategory,name="updateCat"),

    path('product/addproditem',product.addProduct,name="addprod"),
    url(r'^category/(?P<cat_id>\d+)/$',category.getCategory,name='getCat'),
    url(r'^category/(?P<cat_id>\d+)/delete/$',category.ondelete,name='nameDel')
]
