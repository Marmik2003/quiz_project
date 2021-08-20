from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.signup, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
