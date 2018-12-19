from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from electronic.models import Category,Product
# Create your views here.
def listCategory(request):
    all_cat=Category.objects.all()
    return  render(request,'list.html',{'categories': all_cat })



    #return  HttpResponse("hello",all_cat)

def getCategory(request,cat_id):
    data=get_object_or_404(Category,id=cat_id)
    return render(request, 'show.html', {'one_cat': data})
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
        return  render(request,'add.html')
