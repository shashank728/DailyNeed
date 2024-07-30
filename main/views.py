from django.shortcuts import render,redirect

from .models import Todo,Profile
# Create your views here.


# ==================== home =================================

def home(request):
    return render(request,"home.html")

# ==================== todo =================================
def todo(request):
    todo = Todo.objects.all()
    incompleted_todos = todo.filter(complete = False)
    completed_todos = todo.filter(complete = True)
    

    parameter = {
        "todos":incompleted_todos,
        "completed":completed_todos
    }
    return render(request,"todo.html",parameter)

    

# =================== add todo =============================
def addtodo(request):
    if request.method == "POST":
        user_task = request.POST.get("task")
        user_quantity = request.POST.get("quantity")
        
        new_todo = Todo(
            task = user_task,
            quantity = user_quantity   
        )
        new_todo.save()
        return redirect("todo")
    
    return render(request,"addtodo.html")

# ======================== creat profile form ==============================

def creat_profile(request):
    
    if request.method == "POST":
        profile_pic = request.FILES["img"]
        profile_name = request.POST.get("name")
        profile_number = request.POST.get("phone")
    
        info = Profile(
            img = profile_pic,
            name = profile_name,
            number = profile_number
        )
        
        
        info.save()
        return redirect("profile")
    
    return render(request,"creat_profile.html")
    

# ======================== update profile form ==============================

def update_profile_form(request,info_id):
    
    profile = Profile.objects.get(id = info_id)
    
    if request.method == "POST":
        profile.img = request.FILES["img"]
        profile.name = request.POST.get("name")
        profile.number = request.POST.get("number")
      
        profile.save()
        
        return redirect("profile")
        
    
    return render(request,"update_profile.html")


# ======================= profile ==============================

def profile(request):
    
    information = Profile.objects.all()
    
    parameter = {
        "information" : information
    }
    
    return render(request,"profile.html",parameter)

# ========================= DELETE ================================

def delete(request,todo_id):
    todo = Todo.objects.get(id = todo_id)
    
    todo.delete()
    return redirect("todo")

# ========================= update ===============================

def update(request,todo_id):
    
    todo = Todo.objects.get(id = todo_id)
    
    parameter = {
        'todo':todo
    }
    
    if request.method == "POST":
        user_task = request.POST.get("task")
        user_date = request.POST.get("date")
        
        
        todo.task = user_task
        todo.date = user_date
        

        todo.save()
        return redirect("todo")
    

    return render(request,"update_todo.html",parameter)


# ======================= complete task =============================

def complete(request,todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.complete = True
    todo.save()
    
    return redirect("todo")