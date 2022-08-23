from multiprocessing import context
from .models import Contact
from django.shortcuts import render,redirect
from .forms import ContactForm
from products.models import Jenerator
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request,'services.html')


#ürün Yönetimi
# *******************************************************
def contact(request):
   form = ContactForm(request.POST or None)

   if form.is_valid():    
    form.save()
   
   context = {
    "form":form
   }

   return render(request,'contact.html',context)
# *******************************************************   

#ürün Yönetimi
# *******************************************************
@login_required(login_url="user:login")
def dashboard(request):
    products = Jenerator.objects.filter()
    return render(request, 'dashboard-pm.html',{"products":products})
# *******************************************************

#İletişim Mesaj Yönetimi
# *******************************************************************
@login_required(login_url="user:login")
def dashboardCm(request):
    contacts = Contact.objects.filter()
    return render(request, 'dashboard-cm.html', {"contacts":contacts})

# *******************************************************

#İletişim Mesaj Yönetimi
# *******************************************************************
@login_required(login_url="user:login")
def contactDetail(request,id):
    contact = Contact.objects.filter(id=id).first()
    return render(request,'contact-detail.html',{"contact":contact})


#İletişim Mesaj Silme
# *******************************************************************
@login_required(login_url="user:login")
def contactDelete(request,id):
    contact = Contact.objects.filter(id=id).first()
    contact.delete()
    return redirect('dashboard-cm')
