from rest_framework import serializers
from .models import Aluno, Disciplina, Tarefa
# Create your models here.

class AlunoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aluno
    fields = '__all__'

class DisciplinasSerializers(serializers.ModelSerializer):
  class Mata:
    model = Disciplina
    fields = '__all__'

class TarefaSerializers(serializers.ModelSerializer):
  class Meta:
    model = Tarefa
    fields = '__all__'    