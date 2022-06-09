from django.shortcuts import render,HttpResponse,redirect
from .models import student
from .forms import studentform

# Create your views here.

def add(request):
 if request.method == 'POST':
  fm = studentform(request.POST)
  if fm.is_valid():
   fm.save()
   return HttpResponse('Added to database')
 fm = studentform()
 return render(request,'add.html',{'form':fm})

def show(request):
 rs = student.objects.all()
 return render(request,'show.html',{'student':rs})

def edit(request,id):
 if request.method == 'POST':
  rs = student.objects.get(id=id)
  fm = studentform(request.POST,instance=rs)
  if fm.is_valid():
   fm.save()
   return redirect('/show')
 rs = student.objects.get(id=id)
 return render(request,'edit.html',{'s':rs})


