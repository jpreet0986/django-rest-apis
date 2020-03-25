from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'leads'
urlpatterns = [
    path('leads/', views.lead_list_create, name="list"),
    path('leads/<int:pk>/', views.lead_detail, name="detail"),
]
