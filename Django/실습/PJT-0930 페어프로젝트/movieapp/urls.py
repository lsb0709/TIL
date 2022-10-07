from django.urls import path, include
from . import views

app_name = "movieapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("detail/<int:pk_>", views.detail, name="detail"),
    path("delete/<int:pk_>", views.delete, name="delete"),
    path("update/<int:pk_>", views.update, name="update"),
    path("edit/<int:pk_>", views.edit, name="edit"),
    path("heart/<int:pk_>", views.heart, name="heart"),
]
