from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from test_admin.models import ExamSet, ExamResult, ExamFaces, QuestionResponse, Question, ExamQuestion
from users.models import User


@login_required
def index(request):
    if request.method != 'POST':
        exams = ExamSet.objects.all().exclude(examresult__student=request.user)
        return render(request, 'student/index.html', context={
            'exams': exams
        })


@login_required
def exam_prestage(request, exam_id):
    if request.method != 'POST':
        exam = ExamSet.objects.get(id=exam_id)
        return render(request, 'student/exam_prestage.html', context={'exam': exam})


@csrf_exempt
@login_required
def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['file']
        student_user = request.user
        exam = request.POST['exam_id']
        ExamFaces.objects.create(face=image, student=student_user, exam_id=exam)
        return JsonResponse({'response': 'Image uploaded successfully'}, status=200)


@login_required
def attempt_exam(request, exam_id):
    if request.method != 'POST':
        if not ExamFaces.objects.filter(student=request.user, exam_id=exam_id).exists():
            messages.warning(request, 'Please capture image first!')
            return redirect('student:exam_prestage')
        responses = QuestionResponse.objects.filter(exam_id=exam_id, student=request.user).order_by('question_id') \
            .values_list('question', flat=True)
        if responses.exists():
            questions = ExamQuestion.objects.filter(exam_id=exam_id).exclude(question__in=responses)
        else:
            questions = ExamQuestion.objects.filter(exam_id=exam_id)

        if not questions.exists():
            messages.warning(request, 'Questions for this Exam have been finished.')
            return redirect('student:index')
        q_left = questions.count()
        question = questions.first()
        candidates = User.objects.filter(is_staff=False).count()
        total_questions = ExamQuestion.objects.filter(exam_id=exam_id)
        questions_count = len(total_questions)
        correct_answers = 0
        for q1 in total_questions:
            for r1 in responses:
                if r1 == q1.question:
                    if r1.response == q1.question.correct_ans:
                        correct_answers += 1
                    break

        q_no = 1
        for q in total_questions:
            if q.id == question.id:
                break
            q_no += 1

        exam_object = ExamSet.objects.get(id=exam_id)
        time_hr = int(exam_object.duration / 60)
        time_minutes = exam_object.duration - int(exam_object.duration / 60)
        context = {
            'exam': exam_object,
            'questions_count': questions_count,
            'question': question,
            'candidates': candidates,
            'q_no': q_no,
            'q_left': q_left,
            'correct_pr': (round((correct_answers / len(total_questions)) * 100)),
            'time_hr': time_hr,
            'time_minutes': time_minutes
        }
        return render(request, 'student/exam_test.html', context=context)


@login_required
def exam_summary(request, exam_id):
    if request.method != 'POST':
        exam = ExamSet.objects.get(id=exam_id)
        responses = QuestionResponse.objects.filter(student=request.user, exam_id=exam_id)
        exam_result = ExamResult.objects.filter(exam_id=exam_id, student=request.user)
        total_questions = ExamQuestion.objects.filter(exam_id=exam_id)
        correct_answers = 0
        for q1 in total_questions:
            for r1 in responses:
                if r1.question == q1.question:
                    if r1.response == q1.question.correct_ans:
                        correct_answers += 1
                    break
        correct_pr = round((correct_answers / len(total_questions)) * 100)
        candidates = User.objects.filter(is_staff=False).count()
        if exam_result.exists():
            exam_result = exam_result.first()
            time_elapsed_hrs = int(exam_result.time_spent / 3600)
            time_elapsed_mins = int((exam_result.time_spent - time_elapsed_hrs * 3600) / 60)
            time_elapsed_sec = exam_result.time_spent - time_elapsed_mins * 60
            time_hr = int(exam.duration / 60)
            time_minutes = exam.duration - int(exam.duration / 60)
            context = {
                'exam': exam,
                'responses': responses,
                'correct_pr': correct_pr,
                'candidates': candidates,
                'questions_count': total_questions.count(),
                'time_elapsed_hrs': time_elapsed_hrs,
                'time_elapsed_mins': time_elapsed_mins,
                'time_elapsed_sec': time_elapsed_sec,
                'time_hr': time_hr,
                'time_minutes': time_minutes
            }
            return render(request, 'student/exam_summary.html', context=context)
        else:
            return HttpResponse('<h1>You haven\'t finished this Module yet...</h1>')


##############
# AJAX VIEWS #
##############

@csrf_exempt
@login_required
def attempt_question(request):
    if request.method == 'POST':
        choice = request.POST['answer']
        question_id = request.POST['question_id']
        exam_id = request.POST['exam_id']
        QuestionResponse.objects.create(
            response=choice,
            question_id=question_id,
            exam_id=exam_id,
            student=request.user
        )
        responses = QuestionResponse.objects.filter(exam_id=exam_id, student=request.user).order_by('question_id')
        question = Question.objects.get(id=question_id)
        correct_ans = question.correct_ans
        total_questions = ExamQuestion.objects.filter(exam_id=exam_id)
        correct_answers = 0
        for q1 in total_questions:
            for r1 in responses:
                if r1.question == q1.question:
                    if r1.response == q1.question.correct_ans:
                        correct_answers += 1
                    break
        correct_pr = round((correct_answers / len(total_questions)) * 100)
        if 'last_question' in request.POST:
            score = 0
            for q1 in total_questions:
                for r1 in responses:
                    if r1.question == q1.question:
                        if r1.response == q1.question.correct_ans:
                            score += q1.question.points
                        break
            ExamResult.objects.create(
                student=request.user,
                exam_id=exam_id,
                time_spent=int(request.POST['time_elapsed']),
                score=score
            )
        context = {
            'correct_pr': correct_pr,
            'correct_ans': correct_ans,
            'question': question
        }
        return render(request, 'partials/student/get_correct_ans.html', context=context)


@login_required
def get_percent(request):
    exam_id = request.GET.get('exam_id')
    responses = QuestionResponse.objects.filter(exam_id=exam_id, student=request.user).order_by('question_id')
    total_questions = ExamQuestion.objects.filter(exam_id=exam_id)
    correct_answers = 0
    for q1 in total_questions:
        for r1 in responses:
            if r1.question == q1.question:
                if r1.response == q1.question.correct_ans:
                    correct_answers += 1
                break
    correct_pr = round((correct_answers / len(total_questions)) * 100)
    return JsonResponse({'response': correct_pr}, status=200)


@login_required
def finish_exam(request):
    exam_id = request.GET.get('exam_id')
    time_left = request.GET.get('time_left')
    responses = QuestionResponse.objects.filter(exam_id=exam_id, student=request.user).order_by('question_id')
    total_questions = ExamQuestion.objects.filter(exam_id=exam_id)
    correct_answers = 0
    score = 0
    for q1 in total_questions:
        for r1 in responses:
            if r1.question == q1.question:
                if r1.response == q1.question.correct_ans:
                    correct_answers += 1
                    score += q1.question.points
                break
    answers = ['answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7', 'answer8', 'answer9',
               'answer10']
    exam = ExamSet.objects.get(id=exam_id)
    time_elapsed = exam.duration * 60 - int(time_left)
    if not ExamResult.objects.filter(student=request.user, exam_id=exam_id).exists():
        ExamResult.objects.create(
            student=request.user,
            exam_id=exam_id,
            time_spent=time_elapsed,
            score=score
        )

    return JsonResponse({'response': 'Test Submitted Successfully'}, status=200)
