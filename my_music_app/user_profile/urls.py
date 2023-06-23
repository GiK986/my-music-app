from django.urls import path
from my_music_app.user_profile import views

urlpatterns = [
    path("details/", views.details, name="profile details"),
    path("delete/", views.delete, name="profile delete"),
]
