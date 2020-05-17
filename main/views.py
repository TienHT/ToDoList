from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .models import Todo
from user.models import User,UserManager
from django.shortcuts import redirect,reverse
from user.forms import LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        messages.error(request,f'Bạn Cần Đăng Nhập Trước Sử Dụng Dịch Vụ')
        return redirect('user:login')
    else:
        todoItems = Todo.objects.filter(user = request.user).order_by("-added_date")
        lengthItem =Todo.objects.filter(user = request.user,is_completed = False).count()
        lengthItemCompleted =Todo.objects.filter(user = request.user,is_completed = True).count()
        
    return render(request,'main/index.html',{'todoItems':todoItems ,'lengthItem':lengthItem,'lengthItemCompleted':lengthItemCompleted})
@csrf_exempt
@login_required
def add_to_do(request):
    # request list todo in form
    currentDate = timezone.now()
    currentText = request.POST.get('content', False)

    #add list todo in database
    Todo.objects.create(user = request.user,text =currentText,added_date = currentDate )
    return redirect('main:index')
@csrf_exempt
@login_required
def delete_to_do(request,iddelete):
    Todo.objects.get(id =iddelete).delete()
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

