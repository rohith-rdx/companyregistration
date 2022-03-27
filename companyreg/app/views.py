# Create your views here.
import imp
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import *
from app1.models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']
        
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                return redirect('index')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname,email=email,username=username,password=password)
                user.save()
                messages.info(request,'registered successfully')
                return redirect('login_page')
        else:
            return redirect('index')
    else:
        return redirect('index')
    
def login_page(request):
    return render(request,'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.info(request,'logged in successfully')
            return redirect('company')
        else:
            messages.info(request,'incorrect password or username')
            return redirect('login_page')
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    messages.info(request,'logged out successfully')
    return redirect('login_page')




@login_required(login_url='login_page')
def company(request):
    return render(request,'company.html')
@login_required(login_url='login_page')
def register(request):
    try:
        if request.method=='POST':
            cmpnyname=request.POST['cmpnyname']
            type=request.POST['type']
            businessname=request.POST['businessname']
            email=request.POST['email']
            mobno=request.POST['mobno']
            website=request.POST['website']
            city=request.POST['city']
            state=request.POST['state']
            country=request.POST['country']
            pincode=request.POST['pincode']
            logo=request.FILES['logo']
            x = User.objects.get(id=request.user.id)
            
            if companys.objects.filter(userid=x).exists():
        
                return redirect ('company')
            elif companys.objects.filter(businessname=businessname).exists():
                 return redirect ('company')
            else:

                employees=companys(cmpnyname=cmpnyname,type=type,businessname=businessname,email=email,mobno=mobno,website=website,city=city,state=state,country=country,pincode=pincode,logo=logo,userid=x)
                employees.save()

                return redirect('branch')
        else:
            return redirect('company')
    except:
        return redirect('index')
@login_required(login_url='login_page')
def branch(request):
    x = User.objects.get(id=request.user.id)
    emp = companys.objects.get(userid=x)
    mem = branchregister.objects.filter(cmpnyid=emp)
    return render(request,'branch.html',{'emp' : emp,'mem':mem})