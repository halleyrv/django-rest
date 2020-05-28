# Create your views here.
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from api.tasks.serializers import (PersonTasksSerializer, TasksSerializer, TaskSerializer)
from api.models import (Task, Person)


class PeopleTasksViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.prefetch_related('tasks').all()
    serializer_class = PersonTasksSerializer


""" ENDPOINTS
   GET Task/:id/
   PUT Task/:id/
   DELETE Task/:id/
   """


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        try:
            task = self.queryset.get(pk=kwargs["pk"])
            return Response(TasksSerializer(task).data)
        except Task.DoesNotExist:
            return Response(
                data={
                    "message": "Task with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


    def put(self, request, *args, **kwargs):
        try:
            task = self.queryset.get(pk=kwargs["pk"])
            serializer = TasksSerializer()
            updated_task = serializer.update(task, request.data)
            return Response(TasksSerializer(updated_task).data)
        except Task.DoesNotExist:
            return Response(
                data={
                    "message": "Task with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            task = self.queryset.get(pk=kwargs["pk"])
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response(
                data={
                    "message": "Task with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
