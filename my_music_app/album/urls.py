from django.urls import path
from my_music_app.album import views

urlpatterns = [
    path("add/", views.add, name="album add"),
    path("details/<int:pk>/", views.details, name="album details"),
    path("edit/<int:pk>/", views.edit, name="album edit"),
    path("delete/<int:pk>/", views.delete, name="album delete"),
]
