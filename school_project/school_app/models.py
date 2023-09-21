# Importa o módulo 'models' do Django, que é usado para definir modelos de banco de dados.
from django.db import models

# Define o modelo 'Student' que representa informações sobre alunos.
class Student(models.Model):
  # Define um campo 'name' para o nome do aluno com limite de 100 caracteres.
  name = models.CharField(max_length=100)
  # Define um campo 'email' para o e-mail do aluno com validação de e-mail único.
  email = models.EmailField(unique=True)

# Define o modelo 'Discipline' que representa informações sobre disciplinas.
class Discipline(models.Model):
  # Define um campo 'name' para o nome da disciplina com limite de 100 caracteres.
  name = models.CharField(max_length=100)
  # Define um campo 'description' para uma descrição mais detalhada da disciplina.
  description = models.TextField()

# Define o modelo 'Task' que representa informações sobre tarefas.
class Task(models.Model):
  # Define um campo 'title' para o título da tarefa com limite de 100 caracteres.
  title = models.CharField(max_length=100)
  # Define um campo 'description' para uma descrição mais detalhada da tarefa.
  description = models.TextField()
  # Define um campo 'delivery_date' para a data de entrega da tarefa.
  delivery_date = models.DateField()
  # Define um campo 'completed' para indicar se a tarefa está concluída ou não, com padrão como False.
  completed = models.BooleanField(default=False)
  # Define um relacionamento 'student' com o modelo 'Student' usando uma chave estrangeira.
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  # Define um relacionamento 'discipline' com o modelo 'Discipline' usando uma relação Many-to-Many.
  discipline = models.ManyToManyField(Discipline)
