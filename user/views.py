from django.contrib import messages
from django.shortcuts import render,redirect

from .forms import LoginForm

from django.contrib.auth import authenticate,login,logout

def loginUser(request):
    form = LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user= authenticate(username=username, password=password)
        if user is None:
            messages.info(request, 'Kullanıcı Adi veya Şifre Hatalı')
            return render(request, "login.html", context)
        messages.info(request,'Giriş Başarılı')
        login(request,user)
        return redirect('index')
    return render(request,"login.html",context)
    
def logoutUser(request):
    logout(request)
    messages.success(request,'Başarıyla Çıkış Yapıldı')
    return redirect('index')
    