from django.db import models
from django.forms import ModelForm

# Create your models here.

class Importance(models.Model):
    title = models.CharField(max_length=20)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    importance = models.ForeignKey(Importance, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
