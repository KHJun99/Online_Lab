from django.shortcuts import render

# 메인 페이지
def index(request):
    return render(request, 'libraries/index.html')