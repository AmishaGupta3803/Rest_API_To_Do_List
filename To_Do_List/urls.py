from django.urls import path
from .views import *

urlpatterns = [
    path("", api, name="api"),
    path("post-task/", post_task, name="post_task"),
    path("all-tasks/", all_tasks, name="all_tasks"),
    path("update-task/", update_task, name="update_task"),
    path("delete-task/", delete_task, name="delete_task"),
    path("get-task/", get_task, name="get_task")
]
