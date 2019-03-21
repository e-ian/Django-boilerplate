from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.RegisterUser.as_view(), name="registerUser"),
    path('login/',views.LoginUser.as_view(), name='LoginUser')
]