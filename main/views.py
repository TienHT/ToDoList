from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .models import Todo,List
from user.models import User,UserManager
from django.shortcuts import redirect,reverse
from user.forms import LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localtime, now
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        messages.error(request,f'You must log in to continue!')
        return redirect('user:login')
    else:
        listTask = List.objects.filter(user = request.user)
        listTest = Todo.objects.filter(listTask__user = request.user)
        
    
        
    return render(request,'main/index.html',{'listTask':listTask,'listObjToDo':listTest}) 

def indexSpecificTask(request,idSpecificTask):
    if not request.user.is_authenticated:
        messages.error(request,f'You must log in to continue!')
        return redirect('user:login')
    else:
        listSpecificTask = Todo.objects.filter(listTask_id = idSpecificTask)
        listCurrectTask = List.objects.get(id = idSpecificTask)
        listTask = List.objects.filter(user = request.user)
        # lengthItem =Todo.objects.filter(user = request.user,is_completed = False).count()
        # lengthItemCompleted =Todo.objects.filter(user = request.user,is_completed = True).count()
        
    return render(request,'main/indexSpecificTask.html',{'listSpecificTask':listSpecificTask,'listCurrectTask':listCurrectTask,'listTask':listTask}) 
@csrf_exempt
@login_required
def add_list(request):
    # request list todo in form
  
    currentTitle = request.POST.get('content', False)
    currentUser= request.user
    #add list todo in database
    List.objects.create(title =currentTitle,user_id = User.object.get(username = currentUser).id)
    return redirect('main:index')
@csrf_exempt
@login_required
def search(request):
    # request list todo in form
    if request.method =='POST':
        currentInput = request.POST.get('search-input', False)
        listTask = List.objects.filter(user = request.user)
       
        listTest = Todo.objects.filter(listTask__user = request.user,text__icontains=currentInput)
        return render(request,'main/index.html',{'listTask':listTask,'listObjToDo':listTest}) 
    #add list todo in database
    
    return redirect('main:index')
@csrf_exempt
@login_required
def add_to_do(request):
    # request list todo in form
    currentDate = timezone.now()
    currentText = request.POST.get('content', False)
    currentTask = request.POST.get('idTask',False)

    currentDate = request.POST['date-input']
    currentTime = request.POST['time-input']
    if currentDate:
        if currentTime:
            Todo.objects.create(text =currentText,listTask_id =int(currentTask),added_date = currentDate ,due_date = currentDate,due_time = currentTime)
        elif not currentTime:
            Todo.objects.create(text =currentText,listTask_id =int(currentTask),added_date = currentDate ,due_date = currentDate)
    elif not currentDate:
        if currentTime:
            Todo.objects.create(text =currentText,listTask_id =int(currentTask),added_date = currentDate ,due_date = localtime(now()).date(),due_time = currentTime)
        elif not currentTime:
            Todo.objects.create(text =currentText,listTask_id =int(currentTask),added_date = currentDate)
    return redirect('main:index')
@csrf_exempt
@login_required
def delete_to_do(request,iddelete):
    Todo.objects.get(id =iddelete).delete()
    return redirect('main:index')
@csrf_exempt
@login_required
def delete_list(request,idlist):
    List.objects.get(id =idlist).delete()
    return redirect('main:index')
@csrf_exempt
@login_required
def complete_to_do(request,idcomplete):
    item = Todo.objects.get(id =idcomplete)
    item.is_completed = True
    item.save()
    return redirect('main:index')
@csrf_exempt
@login_required
def undo_to_do(request,idundo):
    item = Todo.objects.get(id =idundo)
    item.is_completed = False
    item.save()
    return redirect('main:index')
@csrf_exempt
@login_required
def edit_to_do(request,idedit):
    if request.method == 'POST':
        text = request.POST.get('textEdit')
        description = request.POST.get('des')
        itemedit = Todo.objects.get(id = idedit)
        itemedit.text = text
        itemedit.description = description
        itemedit.save()
        return redirect('main:index')
    else:
        context = {
            'item' : Todo.objects.get(id = idedit)
        }
      
        return render(request,"main/edittodo.html",context)

