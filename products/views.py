
from django.shortcuts import render,redirect,get_object_or_404
from .forms import AddProductForm
from .models import Jenerator
from django.contrib.auth.decorators import login_required

#Ürün Sayfası
# ***************************************************************
def details(request,id):
    
   # product = Jenerator.objects.filter(id=id).first()
     product = get_object_or_404(Jenerator, id=id)
  
     return render(request, 'details.html', {"product":product})
# ***************************************************************

 # ÜRÜN EKLE
 # ****************************************************************** 
@login_required(login_url="user:login")
def addProduct(request):
    if request.method =='POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return redirect('dashboard')
    else:
        form = AddProductForm()    
    context={
        "form":form
    }

    return render(request, 'addproduct.html', context)
  #**************************************************************************
#Güncelleme
#----------------------------------------------------------------------------------------
@login_required(login_url="user:login")
def updateProduct(request,id):
    product = get_object_or_404(Jenerator, id = id)
    
    form = AddProductForm(request.POST or None, request.FILES or None, instance = product)
    
    if form.is_valid():
           form.save()
           return redirect('dashboard')
    else:
        context={
        "form":form
             }

    return render(request, 'update.html',context)
#---------------------------------------------------------------------------

#Silme
#----------------------------------------------------------------------------------------
@login_required(login_url="user:login")
def deleteProduct(request,id):
    product = get_object_or_404(Jenerator, id = id)
    product.delete()
    return redirect('dashboard')
#---------------------------------------------------------------------------




def categories(request):
    products = Jenerator.objects.filter()
    context={
        "products": products
    }
    return render(request, 'categories.html', context)


# Ürürn Kopyala 
# **********************************************
@login_required(login_url="user:login")
def copyProduct(request,id):
    product = get_object_or_404(Jenerator, id = id)
    product.pk = None
    product.engine = product.engine+"(Copy)"
    product.save()
    return redirect('dashboard')

# **********************************************