from django.shortcuts import render
from django.shortcuts import render, redirect  
from equipamento.forms import EquipamentoForm  
from equipamento.models import Equipamento  
# Create your views here.  
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
def show(request):  
    equipamentos = Equipamento.objects.all()  
    return render(request,"show.html",{'equipamentos':equipamentos})  
def edit(request, id):  
    equipamento = Equipamento.objects.get(id=id)  
    return render(request,'edit.html', {'equipamento':equipamento})  
def update(request, id):  
    equipamento = Equipamento.objects.get(id=id)  
    form = EquipamentoForm(request.POST, instance = equipamento)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'equipamento': equipamento})  
def destroy(request, id):  
    equipamento = Equipamento.objects.get(id=id)  
    equipamento.delete()  
    return redirect("/show")  