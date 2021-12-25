from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def index(req):
    return render(req,'login.html')

def dashboard(req):
    return HttpResponse("welcome")

def register(req):
    if req.method == "POST":
        from django.contrib.auth.models import User
        fullname = req.POST.get("full_name", None).split(' ')
        username = req.POST.get("username",None)
        email = req.POST.get("email",None)
        password = req.POST.get("password",None)
        u = User.objects.create_user(username,email,password)
        u.first_name = fullname[0]
        u.last_name = fullname[1]
        u.save()
        return redirect('dashboard')
    if req.method == "GET":
        return render(req,'login.html')
    else:
        raise Http404

def login(req):
    if req.method == "POST":
        from django.contrib.auth import login,authenticate
        username = req.POST.get('username',None)
        password = req.POST.get('password',None)
        user = authenticate(req,username=username,password=password)
        print(user)
        if user is not None:
            login(req,user)
            return redirect('dashboard')
        else:
            return render(req,'login.html',{"error":"Wrong Password !"})