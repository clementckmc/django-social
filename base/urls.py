from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name='home'),
    path('create-post', views.createPost, name='create-post'),
    path('post/<str:pk>', views.post, name="post"),
    path('post/delete/<str:pk>', views.deletePost, name="delete-post"),
    path('post/update/<str:pk>', views.updatePost, name="update-post"),
    path('profile/', views.profile, name="profile"),
]
