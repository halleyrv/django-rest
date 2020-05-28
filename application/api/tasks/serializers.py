from rest_framework import serializers

from api.models import Task, Person


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("name", 'person')


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name',)


class PersonTasksSerializer(serializers.ModelSerializer):
    tasks = TasksSerializer(many=True)

    class Meta:
        model = Person
        fields = ('name', 'tasks')
