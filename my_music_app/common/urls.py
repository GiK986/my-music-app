from django.urls import path
from my_music_app.common import views

urlpatterns = [
    path("", views.index, name="home page"),
]