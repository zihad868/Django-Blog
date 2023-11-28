from django.urls import path
from . import views

app_name = 'Item'

urlpatterns = [
    path('newItem/', views.newItem, name='new-item'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]
