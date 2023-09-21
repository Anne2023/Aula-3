# Importa o módulo 'serializers' do Django REST framework, que é usado para criar serializadores.
from rest_framework import serializers
# Importa os modelos (Student, Discipline, Task) do seu aplicativo para serem usados nos serializadores.
from .models import Student, Discipline, Task

# Define o serializador 'StudentSerializer' para o modelo 'Student'.
class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    # Especifica o modelo a ser serializado, que é 'Student'.
    model = Student
    # Especifica que todos os campos do modelo 'Student' devem ser incluídos na serialização.
    fields = '__all__'

# Define o serializador 'DisciplineSerializer' para o modelo 'Discipline'.
class DisciplineSerializer(serializers.ModelSerializer):
  class Meta:
    # Especifica o modelo a ser serializado, que é 'Discipline'.
    model = Discipline
    # Especifica que todos os campos do modelo 'Discipline' devem ser incluídos na serialização.
    fields = '__all__'

# Define o serializador 'TaskSerializer' para o modelo 'Task'.
class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    # Especifica o modelo a ser serializado, que é 'Task'.
    model = Task
    # Especifica que todos os campos do modelo 'Task' devem ser incluídos na serialização.
    fields = '__all__'


    