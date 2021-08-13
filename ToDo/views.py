from django.shortcuts import redirect, render
from .models import Task
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.


def IndexView(request):
    if request.user.is_authenticated:
        
        if request.method == "POST":
            title = request.POST['title']
            work = request.POST['work']
            is_comp = request.POST['status']
            t1 = Task(username=request.user, title=title, work=work, is_completed=is_comp)
            t1.save()

        task = Task.objects.filter(username=request.user).order_by('is_completed')
        return render(request, 'home.html', {'tasks': task})
    else:
        messages.info(request, 'Please Login First')
        return redirect('/login')

def LoginView(request):
    if request.method=='POST':
        un = request.POST['username']
        pa1 = request.POST['password']

        if User.objects.filter(username=un).exists() :
            user = auth.authenticate(username=un, password=pa1)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Password is WRONG")
                return redirect('/login')
        else :
            messages.info(request, "Username Not Exists")
            return redirect('/login')

    else :
        if request.user.is_authenticated:
            messages.info(request, 'You are already Logged in')
            return redirect('/')
        else:
            return render(request, 'login.html')

def RegisterView(request):
    if request.method == 'POST':
        fn = request.POST['f_name']
        ln = request.POST['l_name']
        emid = request.POST['email']
        un = request.POST['username']
        pa1 = request.POST['pass1']
        pa2 = request.POST['pass2']

        if pa1!=pa2 :
            messages.info(request, "Password and Confirm Password Must be Same")
            return render(request, 'register.html')
        elif User.objects.filter(username=un).exists() :
            messages.info(request, "Username Already Exists")
            return render(request, 'register.html')
        elif User.objects.filter(email=emid).exists() :
            messages.info(request, "Email-Id Already Exists")
            return render(request, 'register.html')
        else:
            user = User.objects.create_user(username=un, password=pa1, email=emid, first_name=fn, last_name=ln)
            user.save()
            stra = "User : '"+un+"' Created Succesfully"
            messages.info(request, stra)
            return redirect('/login')
    else:
        if request.user.is_authenticated:
            messages.info(request, 'For Register Please Logout')
            return redirect('/signout')
        else:    
            return render(request, 'register.html')

def SignoutView(request):
    if request.user.is_authenticated:
        return render(request, 'signout.html')
    else:
        messages.info(request, 'Please Login First')
        return redirect('/login')

def confirmSignout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, 'You are Succesfully Logged Out')
        return redirect('/login')
    else:
        messages.info(request, 'Please Login First')
        return redirect('/login')

def delete(request, id):
   task = Task.objects.get(id = id)
   task.delete()
   return redirect('/')

def edit(request, id):
    task = Task.objects.get(id = id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.work = request.POST['work']
        task.is_completed = request.POST['status']
        task.save()
        return redirect('/')
    else:
        return render(request, 'edit.html', {'task': task})
