from django.contrib import admin
from django.urls import path,include
from .views import VideoView, SearchView

urlpatterns = [
    path("videos/",VideoView.as_view()),
    path('search/',SearchView.as_view())
]
