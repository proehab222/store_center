from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from electronic.models import Category,Product
from django.core.paginator import  Paginator


# Create your views here.
def listCategory(request):
    all_cat=Category.objects.all()
    all_prod=Product.objects.all()
    pageinator=Paginator(all_prod,2)
    page = request.GET.get('page')
    producats=pageinator.get_page(page)
    data={'categories': all_cat ,'products':producats}
    return  render(request,'category_temp/index.html',data)



    #return  HttpResponse("hello",all_cat)

def getCategory(request,cat_id):
    data=get_object_or_404(Category,id=cat_id)
    return render(request, 'category_temp/show.html', {'one_cat': data})
    #try :
    #     data=Category.objects.get(id=cat_id)
    #     return render(request, 'show.html', {'one_cat': data})
    # except Category.DoesNotExist:
    #     return render(request,'404.html')

def ondelete(request,cat_id):
    data = Category.objects.get(id=cat_id)
    data.delete()
    return redirect("elect_ehab:listing")


def addCategory(request):
    if(request.method=='POST'):
        newCat=Category()
        newCat.cat_name=request.POST.get('cat_name')
        newCat.cat_desc=request.POST.get('cat_desc')
        newCat.save()
        return redirect("elect_ehab:listing")
    else:
        return  render(request,'category_temp/add.html')

def updateCategory(request,cat_id):
    data=get_object_or_404(Category,id=cat_id)
    if (request.method == 'POST'):
        data.cat_name=request.POST.get('cat_name')
        data.cat_desc=request.POST.get('cat_desc')
        data.save()
        return redirect("elect_ehab:listing")

    else:

        return render(request, 'category_temp/add.html', {'one_cat': data})
