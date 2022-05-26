from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('contest/', views.contest , name="contest"),
    path('task/', views.task , name="task"),
    path('problems/', views.problems , name="problems"),
    path('submissions/', views.submissions , name="submissions"),
    path('class_list/', views.class_list , name="class_list"),
    path('login/', views.login , name="login"),

]
