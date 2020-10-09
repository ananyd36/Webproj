from django.shortcuts import render,redirect
from .models import Mobile, Toys
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




def index(request):
    # mobile = Mobile()
    return render(request, 'index.html')


def Login_Page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate( username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, "Username or Password incorrect")
            return render(request, 'login.html',context)
    return render(request, 'login.html', context)


def register(request):
    form  = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created successfully for "+ user)

            return redirect('Login_Page')

    context = {'form':form}
    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    return redirect('Login_Page')


def detail(request, id):
    mobile = Mobile.objects.get(pk=id)
    return render(request, 'detail.html', {'mobile':mobile})


def more(request, id):
    toys = Toys.objects.get(pk=id)
    return render(request, 'more.html', {'toys':toys})


def index1(request):
    all_mobile = Mobile.objects.all()
    return render(request, 'index1.html',{'all_mobile':all_mobile})


def index2(request):
    all_toys = Toys.objects.all()
    return render(request, 'index2.html',{'all_toys':all_toys})
