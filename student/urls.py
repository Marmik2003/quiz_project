from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('past_exams/', views.past_exams, name='past_exams'),
    path('preexam/<int:exam_id>/', views.exam_prestage, name='exam_prestage'),
    path('capture_upload/', views.upload_image, name='capture_upload'),
    path('exam_summary/<int:exam_id>/', views.exam_summary, name='exam_summary'),

    path('forums/', views.forum_index, name='forum_index'),
    path('forums/<int:question_id>/', views.question_forum, name='question_forum'),
    path('delete_forum/<int:forum_id>/', views.delete_forum, name='delete_forum'),

    path('attempt_exam/<int:exam_id>/', views.attempt_exam, name='attempt_exam'),
    path('attempt_question/', views.attempt_question, name='attempt_question'),
    path('get_percent/', views.get_percent, name='get_percent'),
    path('finish_exam/', views.finish_exam, name='finish_exam'),
]
