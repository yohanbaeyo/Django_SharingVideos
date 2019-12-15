from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from .views import *

urlpatterns = [
    path('<int:pk>', videoDetail.as_view()),
    path('myVideos', myVideo, name="myVideos"),
    path('myVideos/<int:pk>', myVideoDetail.as_view(), name="myVideoDetail"),
    path('myVideos/<int:pk>/delete', videoDelete),
    path('myVideos/<int:pk>/edit', videoEdit),
    path('myVideos/<int:pk>/delete/yes', videoDeleteConfirm),
    path('videoUpload', videoUpload),
]