from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Default user portfolio
    path('user/<str:username>/', views.home, name='user_home'),  # Specific user portfolio
]
