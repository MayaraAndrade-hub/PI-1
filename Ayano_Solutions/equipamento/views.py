from django.shortcuts import render
from django.shortcuts import render, redirect  
from equipamento.forms import EquipamentoForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import mysql.connector
from equipamento.models import Equipamento  
# Create your views here.  

@login_required(login_url='/login/')
def emp(request):  
    if request.method == "POST":  
        form = EquipamentoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EquipamentoForm()  
    return render(request,'index.html',{'form':form})  

@login_required(login_url='/login/')
def show(request):  
    equipamentos = Equipamento.objects.all()  
    return render(request,"show.html",{'equipamentos':equipamentos}) 




@login_required(login_url='/login/')
def edit(request, id):  
    equipamento = Equipamento.objects.get(id=id)  
    return render(request,'edit.html', {'equipamento':equipamento})  

@login_required(login_url='/login/')
def update(request, id):  
    equipamento = Equipamento.objects.get(id=id)  
    form = EquipamentoForm(request.POST, instance = equipamento)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'equipamento': equipamento}) 

@login_required(login_url='/login/')
def destroy(request, id):  
    equipamento = Equipamento.objects.get(id=id)  
    equipamento.delete()  
    return redirect("/show") 

def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect("/show")
        else:
            messages.error(request, "Usuário ou senha incorretos!")
    return redirect('/login/')   

def logout_user(request):
    logout(request)
    return redirect('/login/')
    


