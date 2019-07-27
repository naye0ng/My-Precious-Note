from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<int:user_id>/', views.people, name='people'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update/',views.update, name='update'),
]