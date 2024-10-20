from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),  # Use the custom login view
]
