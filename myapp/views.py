from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from rest_framework.decorators import api_view
import logging

from .serializers import TaskSerializer
from .models import Task

logger = logging.getLogger(__name__)

# Generic views
# class TaskListCreate(generics.ListCreateAPIView):
#     """
#     View to list and create tasks.
#     """
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()
#     # customize 
#     def delete(self, request, *args, **kwargs):
#         """
#         Delete all tasks.
#         """
#         Task.objects.all().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     View to retrieve, update, or delete a task.
#     """
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()
    
    
# viewset
# class TaskViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing tasks.
#     """
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()


@api_view(["GET"])
def get_tasks(request):
    """
    View to list all tasks.
    """
    finish = request.GET.get("finish")
    print(f"[DEBUG] finish: {finish}")
    if finish == "true":
        logger.debug(f"[get_tasks] Fetching finished tasks.")
        tasks = Task.objects.filter(finish=True)
    else:
        logger.debug(f"[get_tasks] Fetching all tasks.")
        tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_task_detail(request, pk):
    """
    View to retrieve a task by its ID.
    """
    logger.debug(f"[get_task_detail] Fetching task with ID: {pk}")
    try:
        task = get_object_or_404(Task, pk=pk)
    except Http404:
        logger.warning(f"[get_task_detail] Task ID {pk} not found")
        raise
    serializer = TaskSerializer(task)
    return Response(serializer.data)

@api_view(["POST"])
def add_task(request):
    """
    View to create a new task.
    """
    logger.debug(f"[add_task] Creating a new task.")
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_task(request, pk):
    """
    View to update a task.
    """
    logger.debug(f"[update_task] Updating task with ID: {pk}")
    task = get_object_or_404(Task, pk=pk)
    serializer = TaskSerializer(task, data=request.data)
    
    if serializer.is_valid():
        logger.debug(f"[update_task] Valid data received for task {pk}: {serializer.validated_data}")
        updated_task = serializer.save()
        logger.info(f"[update_task] Task {pk} updated successfully.")
        return Response(TaskSerializer(updated_task).data)
    
    logger.warning(f"Invalid data for task {pk}: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_task(request, pk):
    """
    View to delete a task.
    """
    logger.debug(f"[delete_task] Deleting task with ID: {pk}")
    try:
        task = get_object_or_404(Task, pk=pk)
    except Http404:
        logger.warning(f"Tried to delete non-existent task with ID: {pk}")
        raise
    task.delete()
    logger.info(f"[delete_task] Task {pk} deleted successfully.")
    return Response(status=status.HTTP_204_NO_CONTENT)