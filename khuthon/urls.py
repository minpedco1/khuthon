from django.urls import path
from . import views

app_name = 'khuthon'

urlpatterns = [
    path('', views.index),
    path('univBT/', views.univBT),
    path('comBT/', views.comBT),
    path('univBT/leftStudent/', views.leftStudent),
    path('leftUniv/', views.leftUniv),
    path('comBT/rightUniv/', views.rightUniv),
    path('comBT/rightEmp/', views.rightEmp),
]