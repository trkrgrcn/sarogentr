from socket import fromshare
from tkinter.tix import Form
from django import forms

class LoginForm(forms.Form):
    username =forms.CharField(label='kullanıcı adı')
    password = forms.CharField(label='şifre', widget=forms.PasswordInput)
