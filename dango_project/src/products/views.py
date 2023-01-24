from audioop import reverse
from django.shortcuts import render,get_object_or_404,redirect
from django.shortcuts import HttpResponse
from django.http import Http404
from .models import Product
from .forms import ProductForm,RawProductForm

# Create your views here.
def home_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World </h1>")
    return render(request,"home.html",{
        "my_text": "this is about us",
        "my_number": 1234
    })

# def product_create_view(request):
#     print(request.GET['title'])
#     print(request.POST)
#     context={}
#     return render(request,"product/create.html",context)


# def product_create_view(request):
#     my_form=ProductForm()
#     if request.method=="POST":
#          my_form=ProductForm(request.POST)
#          if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#          else:
#             print(my_form.errors)
#     context={
#         "form": my_form
#     }
#     return render(request,"product/create.html",context)



def product_create_view(request):
    form =ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form =ProductForm()
    
    context={
        'form': form
    }
    return render(request,"product/create.html",context)

def product_detail_view(request,my_id):
    # obj=Product.objects.get(id=my_id)
    # obj=get_object_or_404(Product,id=my_id)
    try:
        obj=Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    # context={
    #     'title':obj.title,
    #     'description':obj.description
    # }
    context={
        'object':obj
    }
    return render(request,"product/detail.html",context)




def product_delete_view(request,id):
    obj=get_object_or_404(Product,id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('../../')
    context={
        'object':obj
    }
    return render(request,"product/detail.html",context)

