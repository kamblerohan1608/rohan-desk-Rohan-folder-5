from math import gcd
from unicodedata import name
from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LogInForm,BlogForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import BlogModel
from django.contrib.auth.models import Group,User

# Create your views here.

class home(View):

    def get(self,request):
        form = LogInForm()
        if request.user.is_authenticated is False:
            return render(request,'home.html',{'form':form})
        else:
            return redirect('all_blogs')
        

    def post(self,request):
        form = LogInForm(request.POST,data=request.POST)
        print(form)
        for i in form:
            print(i)
        if form.is_valid():
            print('your data is valid')
            u_name = form.cleaned_data['username']
            u_pass = form.cleaned_data['password']
            print(u_name)
            print(u_pass)
            user = authenticate(username = u_name,password = u_pass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in successfully')
                return redirect('dashboard')
        messages.warning(request,'Something went wrong')
        return render(request,'home.html',{'form':form})


class register(View):

    def get(self,request):
        form = RegisterForm()
        return render(request,'register.html',{'form':form})

    def post(self,request):

        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # g=Group.objects.get(name = 'author')
            # users = User.objects.all()
            # for u in users:       

            messages.success(request,'Registered Successfully')
            return redirect('home')

        return render(request,'register.html',{'form':form})


class dashboard(View):

    def get(self,request):
        if request.user.is_authenticated:
            form = BlogModel.objects.all()
            return render(request,'dashboard.html',{'form':form})
        else:
            return redirect('home')

    def post(self,request):
        return render(request,'dashboard.html')


class signout(View):

    def get(self,request):
        logout(request)
        messages.success(request,'Successfully logged out')
        return redirect('home')

class add_blog(View):
    def get(self,request):
        form = BlogForm()
        return render(request,'add_blog.html',{'form':form})

    def post(self,request):
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Blog Added Successfully')
            return redirect('dashboard')


class all_blogs(View):

    def get(self,request):
        form = BlogModel.objects.all()
        return render(request,'all_blogs.html',{'form': form})


class delete_blog(View):
    
    def get(self,request,pk):
        data = BlogModel.objects.get(id=pk)
        data.delete()
        messages.success(request,'Blog deleted successfully')
        return redirect('dashboard')

class edit_blog(View):

    def get(self,request,pk):
        form = BlogModel.objects.get(id=pk)
        print(form.title)
        print(form.desc)
        return render(request,'edit_blog.html',{'form':form})

    def post(self,request,pk):
        data = BlogModel.objects.get(id=pk)
        title = request.POST['title']
        desc = request.POST['desc']
        # print(title)
        # print(desc)
        # print(data.title)
        # print(data.desc)
        data.title = title
        data.desc = desc
        data.save()
        messages.success(request,'Blog Updated Successfully')
        return redirect('dashboard')




