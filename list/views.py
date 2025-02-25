from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import CustomUser, Todo
from django.contrib.auth.decorators import login_required
from datetime import datetime, date
def main(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    rawData = Todo.objects.filter(user=request.user).order_by("-value" )  # Fetch user's tasks
    rawData_cleaning=list(rawData.values())
    cleanData=[]
    counter=1
    for x in rawData_cleaning:
        x["order"]= counter
        counter+=1
        cleanData.append(x)
    message=False 
    for z in cleanData:
        
        random=z['deadline']-date.today()
        
        
        if random.days <1:
            message="asdkf"
    return render(request, "index.html", {"todos": cleanData, "message": message})

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)  # Authenticate with email

        if user is not None:
            auth_login(request, user)  # Log user in
            return redirect("main")
        else:
            messages.error(request, "Invalid email or password")

    return render(request, "login.html")

def signup_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
        else:
            user = CustomUser.objects.create_user(username=email, email=email, password=password)
            messages.success(request, "Account created successfully! You can log in now.")
            return redirect("login")

    return render(request, "signup.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        priority=request.POST.get("Priority")
        deadline=request.POST.get("Deadline")
        value=value_check(deadline,priority)
        

        if title:
            Todo.objects.create(user=request.user, title=title, priority=priority, deadline=deadline, value=value)
            
    return redirect("main")

@login_required
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.delete()
    return redirect("main")

def value_check(dtime, priority_value):
    today=date.today()
    dtimeRefined=datetime.strptime(dtime, "%Y-%m-%d").date()
    daysBeforeTask=dtimeRefined-today
    refinedData= daysBeforeTask.days
    finalDateData=time_value(refinedData)
    totalPercent=(0.8*float(priority_value))+finalDateData
    return totalPercent/18
    
import math
def time_value(x):
    try:
        return 10 - 9 * (math.log2(x) / math.log2(30))
    except:
        return 0
def about(request):
    return render(request, "about.html")
