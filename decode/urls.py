from django.urls import path
from . import views

urlpatterns = [
    path('decode_url/', views.say_hello)
] 