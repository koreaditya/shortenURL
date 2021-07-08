from django.urls import path
from . import views

urlpatterns = [
    path('encode_url/', views.say_hello)
] 