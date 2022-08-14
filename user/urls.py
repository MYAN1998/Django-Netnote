from django.urls import path

from user import views

urlpatterns = [
    path('login', views.login),
    path('reg', views.reg),
    path('logout/<int:id>', views.logout),
]
