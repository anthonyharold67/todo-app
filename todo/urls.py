from django.urls import path

from .views import Home, TodoCreate, TodoDelete, TodoList, TodoUpdate, isCompleted

urlpatterns = [
    # path("", Home.as_view(),name="home"),
    #- path("",TemplateView.as_view(template_name="todo/home.html"),name="home"),
    path("add",TodoCreate.as_view(),name="add"),
    path("",TodoList.as_view(),name="list"),
    path("update/<int:pk>",TodoUpdate.as_view(),name="update"),
    path("delete/<int:pk>",TodoDelete.as_view(),name="delete"),
    path("completed/<int:id>",isCompleted,name="completed"),
]
