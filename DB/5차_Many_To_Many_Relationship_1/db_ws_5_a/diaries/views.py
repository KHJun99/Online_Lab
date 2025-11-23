from django.shortcuts import render, redirect, get_object_or_404
from .models import Diary, Comment
from .forms import DiaryForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    comment_form = CommentForm()
    context = {
        'diaries': diaries,
        'comment_form': comment_form
    }
    return render(request, 'diaries/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)

@login_required
@require_POST
def like(request, diary_pk):
    diary = get_object_or_404(Diary, pk=diary_pk)

    if request.user in diary.like_users.all():
        diary.like_users.remove(request.user)
    else:
        diary.like_users.add(request.user)
    return redirect('diaries:index')

@login_required
@require_POST
def comments_create(request, diary_pk):
    diary = Diary.objects.get(pk=diary_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.diary = diary
        comment.user = request.user
        comment.save()
    return redirect('diaries:index')

@login_required
@require_POST
def comments_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('diaries:index')