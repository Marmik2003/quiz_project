from ckeditor_uploader.fields import RichTextUploadingFormField
from django import forms

from test_admin.models import Subject, SubjectType, ExamSet, Question


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name',)
        labels = {'name': 'Subject Name'}


class SubjectTypeForm(forms.ModelForm):
    class Meta:
        model = SubjectType
        fields = ('subject', 'type')
        labels = {'subject': 'Subject', 'type': 'Subject Type'}


class ExamSetForm(forms.ModelForm):
    class Meta:
        model = ExamSet
        fields = ('exam_name', 'subject', 'duration')
        labels = {'exam_name': 'Exam Name', 'subject': 'Subject', 'duration': 'Duration (in minutes)'}


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            'question_text', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7', 'answer8',
            'answer9', 'answer10', 'subject', 'subject_type', 'points', 'sq',
            'pr1', 'pr2', 'pr3', 'pr4', 'pr5', 'pr6', 'pr7', 'pr8', 'pr9', 'pr10', 'pr11', 'pr12',
            'sr1', 'sr2', 'sr3', 'sr4', 'sr5', 'sr6', 'sr7', 'sr8', 'sr9', 'sr10', 'correct_ans',
        )
        labels = {'question_text': 'Question', 'answer1': 'answer 1', 'answer2': 'answer 2', 'answer3': 'answer 3',
                  'answer4': 'answer 4', 'answer5': 'answer 5', 'answer6': 'answer 6', 'answer7': 'answer 7',
                  'answer8': 'answer 8', 'answer9': 'answer 9', 'answer10': 'answer 10',
                  'pr1': 'Picture reference 1',
                  'pr2': 'Picture reference 2',
                  'pr3': 'Picture reference 3',
                  'pr4': 'Picture reference 4',
                  'pr5': 'Picture reference 5',
                  'pr6': 'Picture reference 6',
                  'pr7': 'Picture reference 7',
                  'pr8': 'Picture reference 8',
                  'pr9': 'Picture reference 9',
                  'pr10': 'Picture reference 10',
                  'pr11': 'Picture reference 11',
                  'pr12': 'Picture reference 12',
                  'sr1': 'Solution reference 1',
                  'sr2': 'Solution reference 2',
                  'sr3': 'Solution reference 3',
                  'sr4': 'Solution reference 4',
                  'sr5': 'Solution reference 5',
                  'sr6': 'Solution reference 6',
                  'sr7': 'Solution reference 7',
                  'sr8': 'Solution reference 8',
                  'sr9': 'Solution reference 9',
                  'sr10': 'Solution reference 10',
                  'correct_ans': 'CORRECT answer',
                  'sq': 'Special Question'}
        widgets = {
            'question_text': RichTextUploadingFormField(config_name='default'),
            'answer1': RichTextUploadingFormField(),
            'answer2': RichTextUploadingFormField(),
            'answer3': RichTextUploadingFormField(),
            'answer4': RichTextUploadingFormField(),
            'answer5': RichTextUploadingFormField(),
            'answer6': RichTextUploadingFormField(),
            'answer7': RichTextUploadingFormField(),
            'answer8': RichTextUploadingFormField(),
            'answer9': RichTextUploadingFormField(),
            'answer10': RichTextUploadingFormField(),
        }
