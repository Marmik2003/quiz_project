from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

from test_admin.models import Question, ExamSet, ExamQuestion, QuestionResponse, ExamResult, QuestionForum
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('pk', 'email', 'phone', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs


class UserPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'email', 'phone', 'first_name', 'last_name', 'city', 'country']


class GetQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text',
                  'answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7', 'answer8', 'answer9',
                  'answer10', 'correct_ans', 'pr1', 'pr2', 'pr3', 'pr4', 'pr5', 'pr6', 'pr7', 'pr8', 'pr9', 'pr10',
                  'pr11', 'pr12', 'sr1', 'sr2', 'sr3', 'sr4', 'sr5', 'sr6', 'sr7', 'sr8', 'sr9', 'sr10', 'points')


class GetExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSet
        fields = ('exam_name', 'subject', 'duration')


class QuestionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionResponse
        fields = ('exam', 'question', 'response')


class GetQuestionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionResponse
        fields = ('exam', 'question', 'response', 'answered_at')


class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = ('exam', 'score', 'time_spent')


class GetExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = ('exam', 'score', 'time_spent', 'finished_at')


class QuestionForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionForum
        fields = ('question', 'text_title', 'forum_text')


class GetQuestionForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionForum
        fields = ('question', 'text_title', 'forum_text', 'thread_by', 'updated_at')
