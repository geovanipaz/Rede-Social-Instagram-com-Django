from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup')
]
