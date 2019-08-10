from django.shortcuts import render
from .models import list

# Create your views here.
def home(request):  
    return render(request,'index.html',)

def form(request):  
    return render(request,'form.html',)   

def add_details(request):
    print("form submit")
    name = request.POST["name"]
    email = request.POST["email"]
    mobile_number = request.POST["mobile_number"]
    work = request.POST["work"]


    b = list(name=name,email=email,mobile_number=mobile_number,work=work)
    b.save()

    return render(request,'msg.html',)

def record(request):    
    a = list.objects.order_by('name') 
    return render(request,'list.html',{'record':a})

  