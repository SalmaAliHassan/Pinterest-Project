from django.contrib import admin
from django.urls import path,include
from . import views

import pinterest

urlpatterns = [
    path('', views.PinList.as_view()),
    path('<int:pk>', views.PinDetail.as_view()),

    # path('<int:pk>/save', views.PinDetail.as_view()),

    path('users', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),

]
