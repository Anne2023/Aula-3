from django.shortcuts import render
from rest_framework import generics
from .models import Student, Discipline, Task
from .serializers import StudentSerializer, DisciplineSerializer, TaskSerializer
# Create your views here.

class StudentListCreateView(generics.ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class DisciplineListCreateView(generics.ListCreateAPIView):
  queryset = Discipline.objects.all()
  serializer_class = DisciplineSerializer

class DisciplineDatailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Discipline.objects.all()
  serializer_class = DisciplineSerializer

class TaskCreatView(generics.ListCreateAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Task.objects.all()
  serializer_class = TaskSerializer