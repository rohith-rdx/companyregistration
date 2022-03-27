from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from app.models import companys

# Create your views here.
def branchregistration(request):
    emp = companys.objects.all()
    return render(request, 'branchregistration.html',{'emp':emp})

def branchreg(request):
    try:
        if request.method=='POST':
            branchname=request.POST['branchname']
            businessname=request.POST['businessname']
            email=request.POST['email']
            mobno=request.POST['mobno']
            website=request.POST['website']
            city=request.POST['city']
            state=request.POST['state']
            country=request.POST['country']
            pincode=request.POST['pincode']
            password=request.POST['password']
            logo=request.FILES['logo']
            x = companys.objects.get(businessname=businessname)
            
            if branchregister.objects.filter(branchname=branchname).exists():
                return redirect ('branchreg')
    
            else:
                employees=branchregister(branchname=branchname,businessname=businessname,email=email,mobno=mobno,website=website,city=city,state=state,country=country,pincode=pincode,password=password,logo=logo,cmpnyid=x)
                employees.save()
                return redirect ('branchlogin')
        else:
            return redirect('branchregistration')
    except:
        return redirect('branchreg')

def branchlogin(request):
    return render(request, 'branchlogin.html')

def branchlog(request):
    if request.method=='POST':
        if branchregister.objects.filter(branchname=request.POST['branchname'],password=request.POST['password']).exists():
            member=branchregister.objects.get(branchname=request.POST['branchname'], password=request.POST['password'])
            request.session['brid'] = member.branchid
        
            return redirect('employeregistration')
        else:
            return redirect('branchlog')

    else:
        return redirect('branchlog')
def employeregistration(request):
    if request.session['brid'] == "":
        return redirect('branchlogin')
    else:
        brid = request.session['brid']
        var=branchregister.objects.filter(branchid=brid)
        return render(request, 'employeregistration.html',{'var':var})


def employeereg(request):
    if request.session['brid'] == "":
        return redirect('branchlog')
    else:
        try:
            if request.method =='POST':
                name=request.POST['name']
                email=request.POST['email']
                branchname=request.POST['branchname']

                password=request.POST['password']
                phone=request.POST['phone']
                city=request.POST['city']
                state=request.POST['state']
                country=request.POST['country']
                pin=request.POST['pin']
                image=request.FILES['image']

                x=branchregister.objects.get(branchname=branchname)

                if employee.objects.filter(name=name).exists():
                    return redirect('empreg')

                else:
                    emp=employee(name=name,email=email,branchname=branchname,password=password,phone=phone,city=city,state=state,country=country,pin=pin,image=image,branchid=x)
                    emp.save()
                    return redirect('employeeshow')
            else:
                return redirect('empreg')
        except:
            return redirect('empreg')

def employeeshow(request):
    if request.session['brid'] == "":
        return redirect('branchlog')
    else:
        
            brid = request.session['brid']
            empty=employee.objects.filter(branchid=brid)
            return render(request,'employeeshow.html',{'empty':empty})

def delete(request,id):
    if request.session['brid'] == "":
        return redirect('branchlog')
    else:
        employees=employee.objects.get(id=id)
        employees.delete()
        return redirect('employeeshow')
def empedit(request,id):
    if request.session['brid'] == "":
        return redirect('branchlog')
    else:
        brid = request.session['brid']
        mem=employee.objects.get(id=id)
        var=branchregister.objects.filter(branchid=brid)
        return render(request,'empedit.html',{'mem':mem,'var':var})

def update(request,id):
    if request.session['brid'] == "":
        return redirect('branchlog')
    else:
        if request.method == 'POST':
            employees=employee.objects.get(id=id)
            employees.name=request.POST.get('name',employees.name)
            employees.email=request.POST.get('email',employees.email)
            employees.branchname=request.POST.get('branchname',employees.branchname)
            employees.password = request.POST.get('password',employees.password)
            employees.phone = request.POST.get('phone',employees.phone)
            employees.city = request.POST.get('city',employees.city)
            employees.state = request.POST.get('state',employees.state)
            employees.country = request.POST.get('country',employees.country)
            employees.pin = request.POST.get('pin',employees.pin)
            employees.image = request.FILES.get('image',employees.image)
           
            employees.save()
            return redirect('employeeshow')
def logout(request):
    request.session['brid']=""
    if request.session['brid']=="":
        return redirect('branchlogin')
    else:
        pass