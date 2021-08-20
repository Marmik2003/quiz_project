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
]
