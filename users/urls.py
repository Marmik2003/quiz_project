from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.signup, name='sign_up'),
]
