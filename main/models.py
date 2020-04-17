from django.db import models

# Create your models here.
class Todo(models.Model):
    text =models.CharField(max_length = 255)
    added_date =models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
class TaskList(models.Model):
    title = models.CharField(max_length =100)
    todo = models.ForeignKey(Todo,on_delete=models.CASCADE,null = True)