from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


# generic views +
# urlpatterns = [
#     path("", views.TaskListCreate.as_view(), name='get_tasks'),
#     path("<int:pk>/", views.TaskDetail.as_view(), name='task_detail'),
# ]
    
# # viewset
# router = DefaultRouter()
# router.register(r"tasks", views.TaskViewSet, basename="task")
# urlpatterns = router.urls


#  function-based views (@api_view)
urlpatterns = [
    path("", views.get_tasks, name="get_tasks"),
    path("<int:pk>/", views.get_task_detail, name="get_task_detail"),
    path("add/", views.add_task, name="add_task"),
    path("<int:pk>/update/", views.update_task, name="update_task"),
    path("<int:pk>/delete/", views.delete_task, name="delete_task"),
]