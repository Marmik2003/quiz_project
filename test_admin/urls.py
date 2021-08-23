from django.urls import path

from . import views

app_name = 'test_admin'

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('subjects/create/', views.CreateSubject.as_view(), name='create_subject'),
    path('subjects/edit/<int:pk>', views.UpdateSubject.as_view(), name='update_subject'),
    path('subjects/delete/<int:pk>', views.sub_delete, name='delete_sub'),
    path('subject_type/create/', views.CreateSubjectType.as_view(), name='create_subtype'),
    path('subject_type/edit/<int:pk>', views.UpdateSubjectType.as_view(), name='update_subtype'),
    path('subject_type/delete/<int:pk>', views.subject_type_delete, name='delete_subtype'),

    path('create_examset/', views.CreateExamSet.as_view(), name='create_examset'),
    path('update_examset/<int:pk>/', views.UpdateExamSet.as_view(), name='update_examset'),
    path('delete_examset/<int:pk>/', views.examset_delete, name='delete_examset'),

    path('questions/create/', views.CreateQuestion.as_view(), name='create_question'),
    path('questions/update/<int:pk>/', views.UpdateQuestion.as_view(), name='update_question'),
    path('questions/bank/', views.q_bank, name='question_bank'),
    path('questions/add_q', views.add_q_to_exam, name='add_q_to_exam'),

    path('exam_result/', views.exam_result, name='exam_result'),

    # AJAX
    path('load_topics/', views.load_topics, name='load_types'),
    path('table_update/', views.tableupdate, name='tableupdate'),

    path('question_update/', views.questionupdate, name='questionupdate'),
    path('questions/add_q_to_exam/', views.add_question_to_exam_process, name='add_question_to_exam_process'),
    path('questions/add_q_to_exam/remove/',
         views.remove_question_from_exam_process, name='remove_question_from_exam_process'),

    path('get_result/', views.examres_query, name='examres_query'),
]
