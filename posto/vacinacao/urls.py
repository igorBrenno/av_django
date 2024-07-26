from django.urls import path
from . import views

urlpatterns = [
    path('q1', views.q1, name="q1"),
    path('q2', views.q2, name="q2"),
    path('q3', views.q3, name="q3"),
    path('vacinada', views.vacinada, name="vacinada"),
    path('q9', views.q9, name="q9"),
]