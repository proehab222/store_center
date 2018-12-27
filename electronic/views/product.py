
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render

from electronic.models import Product,Category
def addProduct(request):
    if(request.method=='POST'):
        newprod=Product()
        newprod.prod_name=request.POST.get('pro_name')
        newprod.prod_price=request.POST.get('pro_price')
        newprod.prod_photo = request.FILES['pro_photot']
        select_cat=Category.objects.get(id=request.POST.get('selected_Cat'))
        newprod.category=select_cat
        newprod.save()
        return redirect("elect_ehab:listing")
    else:
        all_cat=Category.objects.all()

        return  render(request,'product_temp/add_prod.html',{'allcat':all_cat})

def listProduct(request):
    all_prod=Product.objects.all()
    return  render(request,'product_temp/list_product.html',{'products': all_prod })