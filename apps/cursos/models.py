from turtle import update
from venv import create
from django.db import models

# Create your models here.
class Curso(models.Model):
    curso = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.curso
    
