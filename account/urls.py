from . import views
from django.urls import path
urlpatterns = [
    path('',views.index,name = 'account'),
    path('Login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('dashboard', views.dashboard, name="dashboard"),

]