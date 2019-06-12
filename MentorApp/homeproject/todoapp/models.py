from django.db import models

# Create your models here.

class todolist(models.Model):
    name = models.CharField(max_len=120)
    date = models.DateTimeField(auto_now_add=True)

    def __todolist__(self):
        return todolist

class todoitem(models.Model):
    description = models.CharField(max_length=128)
    due_date = models.DateField(blank=True)
    completed = models.BooleanField()

    listName = models.ForeignKey(todolist,on_delete=models.CASCADE)

    def __todoitem__(self):
        return todoitem
