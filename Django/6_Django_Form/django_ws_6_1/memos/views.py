from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from .forms import MemoForm

def index(request):
    memos = Memo.objects.order_by('-pk')
    return render(request, 'memos/index.html', {'memos': memos})

def new(request):
    form = MemoForm()
    return render(request, 'memos/create.html', {'form': form})  # 파일명 일치!

def create(request):
    if request.method != 'POST':
        return redirect('memos:new')
    form = MemoForm(request.POST)
    if form.is_valid():
        memo = form.save()
        return redirect('memos:detail', memo.pk)
    # 유효성 실패 시 다시 작성 화면
    return render(request, 'memos/create.html', {'form': form})

def detail(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    return render(request, 'memos/detail.html', {'memo': memo})

def delete(request, pk):
    if request.method == 'POST':
        memo = get_object_or_404(Memo, pk=pk)
        memo.delete()
    return redirect('memos:index')
