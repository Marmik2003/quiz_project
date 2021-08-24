from rest_framework import generics, permissions, authentication, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings

from student.api.serializers import GetExamSerializer, GetQuestionSerializer, QuestionResponseSerializer, \
    GetQuestionResponseSerializer, QuestionForumSerializer, GetQuestionForumSerializer, ExamResultSerializer, \
    UserSerializer, AuthTokenSerializer, UserPropertiesSerializer

from test_admin.models import ExamSet, Question, QuestionResponse, ExamQuestion, QuestionForum, ExamResult
from users.models import User


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return get_object_or_404(User, phone=self.request.user.phone)


@api_view(['GET', ])
@permission_classes((permissions.IsAuthenticated,))
@authentication_classes((authentication.TokenAuthentication,),)
def user_properties_view(request):
    try:
        user = request.user
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserPropertiesSerializer(user)
        return Response(serializer.data)


class GetExamView(generics.ListAPIView):
    serializer_class = GetExamSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (authentication.TokenAuthentication, )
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('exam_name', 'subject')

    def get_queryset(self):
        return ExamSet.objects.all().exclude(examresult__student=self.request.user)


class GetQuestionView(generics.RetrieveAPIView):
    serializer_class = GetQuestionSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (authentication.TokenAuthentication, )

    def get_object(self):
        responses = QuestionResponse.objects.filter(exam_id=self.kwargs['exam_id'],
                                                    student=self.request.user).order_by('question_id') \
            .values_list('question', flat=True)
        if responses.exists():
            questions = ExamQuestion.objects.filter(exam_id=self.kwargs['exam_id'])\
                .exclude(question__in=responses).values_list('question', flat=True)
        else:
            questions = ExamQuestion.objects.filter(exam_id=self.kwargs['exam_id']).values_list('question', flat=True)

        return questions.first()


class SaveResponseView(generics.CreateAPIView):
    serializer_class = QuestionResponseSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class ListExamResponsesView(generics.ListAPIView):
    serializer_class = GetQuestionResponseSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return QuestionResponse.objects.filter(exam_id=self.kwargs['exam_id']).order_by('-answered_at')


class CreateExamResultsView(generics.CreateAPIView):
    serializer_class = ExamResultSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class ListExamResultsView(generics.ListAPIView):
    serializer_class = (ExamResultSerializer,)
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return ExamResult.objects.filter(student=self.request.user)


class ListQuestionForumView(generics.ListAPIView):
    serializer_class = GetQuestionForumSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return QuestionForum.objects.filter(question_id=self.kwargs['question_id']).order_by('-updated_at')


class CreateQuestionForumView(generics.CreateAPIView):
    serializer_class = QuestionForumSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(thread_by=self.request.user)


class ManageQuestionForumView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionForumSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return QuestionForum.objects.filter(thread_by=self.request.user)

    def get_object(self):
        """Retrieve and return barber"""
        if 'pk' in self.kwargs:
            self.lookup_field = 'pk'
        return super(ManageQuestionForumView, self).get_object()
