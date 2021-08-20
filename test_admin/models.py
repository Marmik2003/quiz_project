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
    question_test = RichTextUploadingField()
    pr1 = models.ImageField(null=True, blank=True, upload_to='problems/img/')
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

    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    points = models.IntegerField()
    CORRECT_ANS = models.CharField(max_length=100, choices=(
        ('answer1', 'answer1'), ('answer2', 'answer2'), ('answer3', 'answer3'), ('answer4', 'answer4'),
        ('answer5', 'answer5'), ('answer6', 'answer6'), ('answer7', 'answer7'), ('answer8', 'answer8'),
        ('answer9', 'answer9'), ('answer10', 'answer10')
    ))
    solution_details = RichTextUploadingField()

    def __str__(self):
        return self.question_test


class ExamSet(models.Model):
    exam_name = models.CharField(max_length=150)
    subject = models.ForeignKey("Subject", on_delete=models.SET_NULL, null=True)
    exam_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    duration = models.IntegerField()

    def __str__(self):
        return self.exam_name


class ExamQuestion(models.Model):
    exam = models.ForeignKey("ExamSet", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
