from django.shortcuts import render
from django.http import  HttpResponse
from electronic.models import Category,Product
# Create your views here.
def listCategory(request):
    all_cat=Category.objects.all()
    return  render(request,'cat.html',{'categories': all_cat })



    #return  HttpResponse("hello",all_cat)

def getCategory(request,cat_id):
    data=Category.objects.get(id=cat_id)
    return render(request, 'show.html', {'one_cat': data})

