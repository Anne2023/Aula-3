from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)

class Discipline(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()

class Task(models.Model):
  title = models.CharField(max_length=100) 
  description = models.TextField()
  delivery_date = models.DateField()
  completed = models.BooleanField(default=False) 
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  discipline = models.ManyToManyField(Discipline)