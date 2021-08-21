from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from test_admin.models import ExamSet, ExamResult


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


