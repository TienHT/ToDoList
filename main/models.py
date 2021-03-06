from django.db import models
from user.models import User
from django.conf import settings
from django.utils import timezone
# Create your models here.

class List(models.Model):
    title = models.CharField(max_length = 255,default = 'Daily Activities')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default = None,blank = True,null=True)
    added_date =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    

class Todo(models.Model):
    text =models.CharField(max_length = 255)
    listTask = models.ForeignKey(List,on_delete=models.CASCADE,default = None,blank = True,null=True)
    due_date = models.DateField(default = None,blank = True,null=True)
    due_time = models.TimeField(default = None,blank = True,null=True)
    added_date =models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='')
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text + ' of ' +self.listTask.title
