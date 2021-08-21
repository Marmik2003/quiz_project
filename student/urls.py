from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('preexam/<int:exam_id>/', views.exam_prestage, name='exam_prestage'),
    path('capture_upload/', views.exam_prestage, name='capture_upload'),
]
