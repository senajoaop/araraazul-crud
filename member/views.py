from django.shortcuts import render, redirect  
from member.forms import MemberForm  
from member.models import Member  


def memb(request):  
    if request.method == "POST":  
        form = MemberForm(request.POST)  

        if form.is_valid():  
            try:  
                form.save()  

                return redirect('/show')  

            except:  
                pass  
    else:  
        form = MemberForm()  

    return render(request, 'index.html', {'form': form})  


def show(request):  
    members = Member.objects.all()  

    return render(request, "show.html", {'members': members})  


def edit(request, id):  
    member = Member.objects.get(id=id)  

    return render(request, 'edit.html', {'member': member})  


def update(request, id):
    member = Member.objects.get(id=id)  
    form = MemberForm(request.POST, instance=member)  

    if form.is_valid():
        form.save()

        return redirect("/show")  

    return render(request, 'edit.html', {'member': member})  


def destroy(request, id):  
    member = Member.objects.get(id=id)  
    member.delete()  

    return redirect("/show")
