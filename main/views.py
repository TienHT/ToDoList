from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .models import Todo
# Create your views here.
def index(request):

    todoItems = Todo.objects.all().order_by("-added_date")
    lengthItem =Todo.objects.all().count()
    return render(request,'main/index.html',{'todoItems':todoItems ,'lengthItem':lengthItem})
@csrf_exempt
def add_to_do(request):
    # request list todo in form
    currentDate = timezone.now()
    currentText = request.POST.get('content', False)
    #add list todo in database
    Todo.objects.create(text =currentText,added_date = currentDate )
    todoItems = Todo.objects.all().order_by("-added_date")
    lengthItem =Todo.objects.all().count()
    return render(request,'main/index.html',{'todoItems':todoItems ,'lengthItem':lengthItem})
@csrf_exempt
def delete_to_do(request,iddelete):
    Todo.objects.get(id =iddelete).delete()
    todoItems = Todo.objects.all().order_by("-added_date")
    lengthItem =Todo.objects.all().count()
    return render(request,'main/index.html',{'todoItems':todoItems ,'lengthItem':lengthItem})