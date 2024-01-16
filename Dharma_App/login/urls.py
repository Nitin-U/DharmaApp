from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('basepage', views.basepage, name="basepage"),
    path('register', views.register, name="register"),
    path('my_login', views.my_login, name="my_login"),
    path('my_logout', views.my_logout, name="my_logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('update_user', views.update_user, name="update_user"),

]