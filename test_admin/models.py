from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class SubjectType(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class Question(models.Model):
    question_text = RichTextUploadingField()
    pr1 = models.ImageField(null=True, blank=True, upload_to='problems/img/')
    pr2 = models.ImageField(null=True, blank=True, upload_to='problems/img/')
    pr3 = models.ImageField(null=True, blank=True, upload_to='problems/img/')
    pr4 = models.ImageField(null=True, blank=True, upload_to='problems/img/')
    pr5 = models.ImageField(null=True, blank=True, upload_to='problems/img/')
    pr6 = models.ImageField(null=True, blank=True, upload_to='problems/img/')
    pr7 = models.ImageField(null=True, blank=True, upload_to='problems/img/')
    pr8 = models.ImageField(null=True, blank=True, upload_to='problems/img/')
    pr9 = models.ImageField(null=True, blank=True, upload_to='problems/img/')
    pr10 = models.ImageField(null=True, blank=True, upload_to='problems/img/')
    pr11 = models.ImageField(null=True, blank=True, upload_to='problems/img/')
    pr12 = models.ImageField(null=True, blank=True, upload_to='problems/img/')
    answer1 = RichTextUploadingField(null=True, blank=True)
    answer2 = RichTextUploadingField(null=True, blank=True)
    answer3 = RichTextUploadingField(null=True, blank=True)
    answer4 = RichTextUploadingField(null=True, blank=True)
    answer5 = RichTextUploadingField(null=True, blank=True)
    answer6 = RichTextUploadingField(null=True, blank=True)
    answer7 = RichTextUploadingField(null=True, blank=True)
    answer8 = RichTextUploadingField(null=True, blank=True)
    answer9 = RichTextUploadingField(null=True, blank=True)
    answer10 = RichTextUploadingField(null=True, blank=True)
    sr1 = models.ImageField(null=True, blank=True, upload_to='solutions/img/')
    sr2 = models.ImageField(null=True, blank=True, upload_to='solutions/img/')
    sr3 = models.ImageField(null=True, blank=True, upload_to='solutions/img/')
    sr4 = models.ImageField(null=True, blank=True, upload_to='solutions/img/')
    sr5 = models.ImageField(null=True, blank=True, upload_to='solutions/img/')
    sr6 = models.ImageField(null=True, blank=True, upload_to='solutions/img/')
    sr7 = models.ImageField(null=True, blank=True, upload_to='solutions/img/')
    sr8 = models.ImageField(null=True, blank=True, upload_to='solutions/img/')
    sr9 = models.ImageField(null=True, blank=True, upload_to='solutions/img/')
    sr10 = models.ImageField(null=True, blank=True, upload_to='solutions/img/')
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    points = models.IntegerField()
    correct_ans = models.CharField(max_length=100, choices=(
        ('answer1', 'answer1'), ('answer2', 'answer2'), ('answer3', 'answer3'), ('answer4', 'answer4'),
        ('answer5', 'answer5'), ('answer6', 'answer6'), ('answer7', 'answer7'), ('answer8', 'answer8'),
        ('answer9', 'answer9'), ('answer10', 'answer10')
    ))
    solution_details = RichTextUploadingField()
    sq = models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subject_type = models.ForeignKey(SubjectType, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class ExamSet(models.Model):
    exam_name = models.CharField(max_length=150)
    subject = models.ForeignKey("Subject", on_delete=models.SET_NULL, null=True)
    exam_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.exam_name


class ExamFaces(models.Model):
    exam = models.ForeignKey(ExamSet, on_delete=models.CASCADE)
    face = models.ImageField(upload_to='student_faces/')


class ExamQuestion(models.Model):
    exam = models.ForeignKey("ExamSet", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class QuestionResponse(models.Model):
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    exam = models.ForeignKey(ExamSet, on_delete=models.CASCADE)
    response = models.CharField(max_length=10)
    answered_at = models.DateTimeField(auto_now_add=True)


class ExamResult(models.Model):
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    exam = models.ForeignKey(ExamSet, on_delete=models.CASCADE)
    finished_at = models.DateTimeField(auto_now_add=True)
    time_spent = models.PositiveIntegerField(default=0)
    score = models.FloatField(default=0)


class QuestionForum(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    forum_text = RichTextUploadingField()
    thread_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.forum_text


class ForumReply(models.Model):
    forum = models.ForeignKey(QuestionForum, on_delete=models.CASCADE)
    forum_text = RichTextUploadingField()
    thread_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.forum_text
