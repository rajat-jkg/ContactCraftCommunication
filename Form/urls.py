from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-new-form/', views.AddNewForm.as_view(), name='add-form')
]