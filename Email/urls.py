from django.urls import path

from Email import views

urlpatterns = [
    path('send/', views.send)

]