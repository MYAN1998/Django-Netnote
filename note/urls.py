from django.urls import path

from note import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('mod/', views.mod),
    path('delete/<int:id>', views.delete),
]
