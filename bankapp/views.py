
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from .models import Branches, Districts, Form
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy


#

# class DistrictCreateView(CreateView):
#  fields = ('district')
#  success_url = reverse_lazy('District_changelist')


# class DistrictUpdateView(UpdateView):
#   model = Districts
# success_url = reverse_lazy('District_changelist')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'new.html')
        else:
            messages.info(request, "invalid credentials")
            return redirect('bank:login')

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['password']
        cpwd = request.POST['cpassword']
        user = authenticate(request,username=username, password=pwd)
        if len(username)<=0 or len(pwd)<=0:
            messages.info(request, "Fields are required")
            return redirect('bank:register')
        else:
            if pwd == cpwd:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already taken")
                    return redirect('bank:register')
                else:
                    user = User.objects.create_user(username=username, password=pwd)
                    user.save()
                    return redirect("bank:login")
            else:
                messages.info(request, "password does not match")
                return redirect("bank:register")
    return render(request, "register.html")


def display(request):
    return render(request, "home.html")


def form_view(request):
    districts = Districts.objects.all()
    branches = Branches.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        dob=request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phoneNo = request.POST.get('phoneNo')
        emailId = request.POST.get('emailId')
        address = request.POST.get('address')
        district = request.POST.get('district1')
        branch = request.POST.get('branch1')
        accountType = request.POST.get('accountType')
        materials = request.POST.getlist('materials')
        if len(name) <= 0 or len(age) <= 0 or len(dob) <= 0 or len(gender) <= 0 or len(phoneNo) <= 0 or len(emailId) <= 0 or len(address) <= 0 :
            messages.info(request,"You must fill the form completely")
            return render(request,'logoutpage.html')
        else:
            form = Form(name=name, dob=dob, age=age, gender=gender, phoneNo=phoneNo, emailId=emailId, address=address,
                        district=district, branch=branch, accountType=accountType, materials=materials)

            form.save()
        messages.success(request, 'Application submitted successfully')
        return render(request,'logoutpage.html')
    return render(request, "form.html", {'district': districts, 'branches': branches})


















