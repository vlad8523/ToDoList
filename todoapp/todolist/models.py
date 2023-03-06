from django.db import models
from django.forms import ModelForm

# Create your models here.

IMPORTANCE_CHOICE = [
    ('imp', 'Important'),
    ('nim', 'Not important'),

]

class Importance(models.Model):

    def __str__(self):
        pass

class Task(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    importance = models.CharField(max_length=3, choices=IMPORTANCE_CHOICE, default='nim')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # def get_importance_display():
    #     pass

# class TaskForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title','complete','importance','created']
