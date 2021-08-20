from django import forms

from test_admin.models import Subject, SubjectType


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name',)
        labels = {'name': 'Subject Name'}


class SubjectTypeForm(forms.ModelForm):
    class Meta:
        model  = SubjectType
        fields = ('subject', 'type')
        labels = {'subject': 'Subject', 'type': 'Subject Type'}
