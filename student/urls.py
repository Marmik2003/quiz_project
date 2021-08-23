from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('preexam/<int:exam_id>/', views.exam_prestage, name='exam_prestage'),
    path('capture_upload/', views.upload_image, name='capture_upload'),
    path('exam_summary/<int:exam_id>/', views.exam_summary, name='exam_summary'),

    path('attempt_exam/<int:exam_id>/', views.attempt_exam, name='attempt_exam'),
    path('attempt_question/', views.attempt_question, name='attempt_question'),
    path('get_percent/', views.get_percent, name='get_percent'),
    path('finish_exam/', views.finish_exam, name='finish_exam'),
]
