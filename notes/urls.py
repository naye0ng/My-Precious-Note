from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.index, name='list'),
    path('<int:notes_id>/like/', views.like, name='like'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]

