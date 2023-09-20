from django.urls import path
from .views import StudentListCreatView, StudentDetailView, DisciplineListCreateView, DisciplineDatailView, TaskCreatView, TaskDetailView
from django.contrib import admin
from django.urls import path, include

urlpatternes = [
  path('student/', StudentListCreatView.as_view(),name='student-list-create'),
  path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
  path('discipline/', DisciplineListCreateView.as_view(), name='discipline-list-create'),
  path('discipline/<int:pk>/', DisciplineDatailView.as_view(), name='discipline-detail'),
  path('task/', TaskCreatView.as_view(), name='task-list-create'),
  path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
  path('admin/', admin.site.urls),
  path('api/', include('school_app.urls')),
]