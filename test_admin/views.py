from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from test_admin.forms import SubjectForm, SubjectTypeForm
from test_admin.models import Subject, SubjectType


class DashboardView(UserPassesTestMixin, TemplateView):

    template_name = "test_admin/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def test_func(self):
        return self.request.user.is_superuser


class CreateSubject(UserPassesTestMixin, CreateView, SuccessMessageMixin):
    model = Subject
    form_class = SubjectForm
    template_name = 'test_admin/add_subject.html'
    success_url = reverse_lazy('test_admin:create_subject')
    success_message = 'Subject Created successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all().order_by('-id')
        return context

    def test_func(self):
        return self.request.user.is_superuser


class UpdateSubject(UserPassesTestMixin, UpdateView, SuccessMessageMixin):
    model = Subject
    form_class = SubjectForm
    template_name = 'test_admin/add_subject.html'
    success_url = reverse_lazy('test_admin:create_subject')
    success_message = 'Subject Edited successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all().order_by('-id')
        return context

    def test_func(self):
        return self.request.user.is_superuser


@login_required
@user_passes_test(lambda u: u.is_superuser)
def sub_delete(request, pk):
    subject = Subject.objects.get(id=pk)
    subject.delete()
    messages.success(request, 'Subject Deleted Successfully!')
    return redirect('test_admin:create_subject')


class CreateSubjectType(UserPassesTestMixin, CreateView, SuccessMessageMixin):
    model = SubjectType
    form_class = SubjectTypeForm
    template_name = 'test_admin/add_type.html'

    def get_form(self, form_class=None):
        form = super(CreateSubjectType, self).get_form(form_class)
        form.fields['subject'].queryset = Subject.objects.all()
        return form
    success_url = reverse_lazy('test_admin:create_subtype')
    success_message = 'Subject Type Created successfully!'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = SubjectType.objects.all().order_by('-id')
        return context


class UpdateSubjectType(UserPassesTestMixin, UpdateView, SuccessMessageMixin):
    model = SubjectType
    form_class = SubjectTypeForm

    def get_form(self, form_class=None):
        form = super(UpdateSubjectType, self).get_form(form_class)
        form.fields['subject'].queryset = Subject.objects.all()
        return form
    template_name = 'test_admin/add_type.html'
    success_url = reverse_lazy('test_admin:create_subtype')
    success_message = 'Subject Type edited successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = SubjectType.objects.all().order_by('id')
        return context

    def test_func(self):
        return self.request.user.is_superuser


@login_required
@user_passes_test(lambda u: u.is_superuser)
def subject_type_delete(request, pk):
    sub_type = SubjectType.objects.get(id=pk)
    sub_type.delete()
    messages.success(request, 'Subject type Deleted Successfully!')
    return redirect('test_admin:create_subtype')



