from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from test_admin.forms import SubjectForm, SubjectTypeForm, ExamSetForm, QuestionForm
from test_admin.models import Subject, SubjectType, ExamSet, Question, ExamQuestion, ExamResult


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


class CreateExamSet(UserPassesTestMixin, CreateView, SuccessMessageMixin):
    model = ExamSet
    form_class = ExamSetForm
    template_name = 'test_admin/create_examset.html'
    success_url = reverse_lazy('test_admin:create_examset')
    success_message = 'Exam set created Successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['examsets'] = ExamSet.objects.all().order_by('-id')
        return context

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.exam_by_id = self.request.user.id
        obj.save()
        messages.success(self.request, 'ExamSet Created Successfully!')
        return super().form_valid(form)


class UpdateExamSet(UserPassesTestMixin, UpdateView, SuccessMessageMixin):
    model = ExamSet
    form_class = ExamSetForm
    template_name = 'test_admin/create_examset.html'
    success_url = reverse_lazy('test_admin:create_examset')
    success_message = 'Exam set edited Successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['examsets'] = ExamSet.objects.all().order_by('-id')
        return context

    def test_func(self):
        return self.request.user.is_superuser


@login_required
@user_passes_test(lambda u: u.is_superuser)
def examset_delete(request, pk):
    examset = ExamSet.objects.get(id=pk)
    examset.delete()
    messages.success(request, 'Exam set Deleted Successfully!')
    return redirect('test_admin:create_subtype')


class CreateQuestion(UserPassesTestMixin, CreateView, SuccessMessageMixin):
    model = Question
    form_class = QuestionForm
    template_name = 'test_admin/add_question.html'
    success_url = reverse_lazy('test_admin:create_question')
    success_message = 'Question Added successfully!'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner_id = self.request.user.id
        obj.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class UpdateQuestion(UserPassesTestMixin, UpdateView, SuccessMessageMixin):
    model = Question
    form_class = QuestionForm
    template_name = 'test_admin/add_question.html'
    success_url = reverse_lazy('test_admin:create_question')
    success_message = 'Question Edited successfully!'

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update stories """
        obj = self.get_object()
        if obj.owner_id != self.request.user.id:
            return redirect(obj)
        return super(UpdateQuestion, self).dispatch(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_superuser


@login_required
@user_passes_test(lambda u: u.is_superuser)
def question_delete(request, pk):
    try:
        question = Question.objects.get(id=pk)
    except ObjectDoesNotExist:
        messages.error(request, 'This Question does not exist!')
        return redirect('test_admin:create_question')
    if question.owner.id == request.user.id:
        question.delete()
        messages.success(request, 'Exam set Deleted Successfully!')
    else:
        messages.error(request, 'Validation failed')
    return redirect('test_admin:create_subtype')


########
# AJAX #
########
@login_required
@user_passes_test(lambda u: u.is_superuser)
def load_topics(request):
    sub_id = request.GET.get('subject')
    types = SubjectType.objects.filter(
        subject_id=sub_id)
    return render(request, 'partials/test_admin/subject_type_dr.html', {'types': types})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_question_to_exam_process(request):
    exam_id = request.GET.get('exam_id')
    question_id = request.GET.get('question_id')
    examquestion_query = ExamQuestion(
        exam_id=exam_id, question_id=question_id)
    examquestion_query.save()
    return JsonResponse({'response': 'successfully added'}, status=200)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def remove_question_from_exam_process(request):
    exam_id = request.GET.get('exam_id')
    question_id = request.GET.get('question_id')
    examquestion_query = ExamQuestion.objects.filter(
        question_id=question_id, exam_id=exam_id)
    examquestion_query.delete()
    return JsonResponse({'response': 'successfully removed'}, status=200)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def q_bank(request):
    questions = Question.objects.filter(
        owner_id=request.user.id)
    subjects = Subject.objects.all()
    return render(request, 'test_admin/q_bank.html', context={'questions': questions, 'subjects': subjects})


def tableupdate(request):
    if request.GET.get('subject'):
        subject = request.GET.get('subject')
        questions = Question.objects.filter(
            owner_id=request.user.id, subject_id=subject)
    elif request.GET.get('sub_type'):
        sub_type = request.GET.get('sub_type')
        questions = Question.objects.filter(
            owner_id=request.user.id, subject_type_id=sub_type)
    else:
        questions = Question.objects.all()
    return render(request, 'partials/test_admin/qb_table.html', context={'questions': questions})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_q_to_exam(request):
    if request.method != 'POST':
        exams = ExamSet.objects.all()
        subjects = Subject.objects.all()
        context = {'exams': exams, 'subjects': subjects}
        return render(request, 'test_admin/add_q_to_exam.html', context=context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def questionupdate(request):
    if request.GET.get('dr_scheduled_exam'):
        scheduled_exam = int(request.GET.get('dr_scheduled_exam'))
        questions = Question.objects.filter(owner_id=request.user.id)
        try:
            exam_questions = [question.question_id for question in ExamQuestion.objects.filter(
                exam_id=scheduled_exam)]
        except:
            exam_questions = []
        context = {'questions': questions, 'exam_questions': exam_questions,
                   'scheduled_exam': scheduled_exam}
        return render(request, 'partials/test_admin/question_table_update.html', context=context)
    elif request.GET.get('dr_scheduled_exam1'):
        scheduled_exam = int(request.GET.get('dr_scheduled_exam1'))
        subject_id = request.GET.get('subject')
        questions = Question.objects.filter(
            owner_id=request.user.id, subject_id=subject_id)
        exam_questions = [question.question_id for question in ExamQuestion.objects.filter(
            exam_id=scheduled_exam)]
        context = {'questions': questions, 'exam_questions': exam_questions,
                   'scheduled_exam': scheduled_exam}
        return render(request, 'partials/test_admin/question_table_update.html', context=context)
    elif request.GET.get('dr_scheduled_exam2'):
        scheduled_exam = int(request.GET.get('dr_scheduled_exam2'))
        subject_type_id = request.GET.get('sub_type')
        questions = Question.objects.filter(
            owner_id=request.user.id, subject_type_id=subject_type_id)
        exam_questions = [question.question_id for question in ExamQuestion.objects.filter(
            exam_id=scheduled_exam)]
        context = {'questions': questions, 'exam_questions': exam_questions,
                   'scheduled_exam': scheduled_exam}
        return render(request, 'partials/test_admin/question_table_update.html', context=context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def exam_result(request):
    exams = ExamSet.objects.all()
    context = {'exams': exams}
    return render(request, 'test_admin/exam_result.html', context=context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def examres_query(request):
    exam_id = request.GET.get('examid')
    exam_res = ExamResult.objects.filter(exam_id=exam_id)
    questions = ExamQuestion.objects.filter(exam_id=exam_id)
    faces = ExamSet.objects.get(id=exam_id).examfaces_set.all()
    quest_count = questions.count()
    total_marks = 0
    for q in questions:
        total_marks += int(q.question.points)
    context = {'students': exam_res,
               'quest_count': quest_count, 'total_marks': total_marks,
               'faces': faces}
    return render(request, 'partials/test_admin/examres_query.html', context=context)
