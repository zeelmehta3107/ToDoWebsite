from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView, name='Home'),
    path('login/', views.LoginView, name='login'),
    path('register/', views.RegisterView, name='register'),
    path('signout/', views.SignoutView, name='signout'),
    path('confirmSignout/', views.confirmSignout, name='logout'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
]
