from django.urls import path
from . import views
from user import views as user_view
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
   
]