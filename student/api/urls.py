from django.urls import path

from student.api.views import CreateUserView, CreateTokenView, ManageUserView, user_properties_view, GetExamView, \
    GetQuestionView, SaveResponseView, ListExamResponsesView, CreateExamResultsView, ListExamResultsView, \
    ListQuestionForumView, CreateQuestionForumView, ManageQuestionForumView

app_name = 'student_api'

urlpatterns = [
    path('users/create/', CreateUserView.as_view(), name='create'),
    path('users/token/', CreateTokenView.as_view(), name='token'),
    path('users/me/', ManageUserView.as_view(), name='me'),
    path('users/me/properties/', user_properties_view, name='user_properties'),

    path('exams/', GetExamView.as_view()),
    path('exams/<int:exam_id>/', GetQuestionView.as_view()),
    path('exams/response/save/', SaveResponseView.as_view()),
    path('exams/responses/<int:exam_id>/', ListExamResponsesView.as_view()),
    path('exams/result/create/', CreateExamResultsView.as_view()),
    path('exams/results/', ListExamResultsView.as_view()),
    path('forums/question/<int:question_id>/', ListQuestionForumView.as_view()),
    path('forums/question/create/<int:question_id>/', CreateQuestionForumView.as_view()),
    path('forums/question/manage/<int:question_id>/', ManageQuestionForumView.as_view()),
]
