from rest_framework import serializers
from .models import Student, Discipline, Task
# Create your models here.

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = '__all__'

class DisciplineSerializers(serializers.ModelSerializer):
  class Mata:
    model = Discipline
    fields = '__all__'

class TaskSerializers(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'    

    