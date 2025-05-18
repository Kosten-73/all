### views.py (в testapp)
from django.shortcuts import render, redirect
from .models import Question, UserAnswer
from .forms import TestForm
from django.contrib.auth.decorators import login_required

@login_required
def test_view(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        form = TestForm(request.POST, questions=questions)
        if form.is_valid():
            for question in questions:
                answer_text = form.cleaned_data.get(f'question_{question.id}')
                UserAnswer.objects.create(
                    user=request.user,
                    question=question,
                    answer=answer_text
                )
            return redirect('results')
    else:
        form = TestForm(questions=questions)
    return render(request, 'testapp/test.html', {'form': form})

@login_required
def results_view(request):
    from django.db.models import Count, Q
    from django.contrib.auth.models import User

    users = User.objects.all()
    data = []
    for user in users:
        answers = UserAnswer.objects.filter(user=user)
        correct = sum(1 for a in answers if a.is_correct())
        data.append({'username': user.username, 'correct': correct})
    return render(request, 'testapp/results.html', {'data': data})

@login_required
def admin_answers_view(request):
    if not request.user.is_superuser:
        return redirect('test')
    answers = UserAnswer.objects.select_related('user', 'question')
    return render(request, 'testapp/admin_answers.html', {'answers': answers})

