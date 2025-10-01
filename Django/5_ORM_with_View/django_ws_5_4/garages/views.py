from django.shortcuts import render, redirect
from .models import Garage

def index(request):
    garages = Garage.objects.all()
    return render(request, 'garages/index.html', {'garages': garages})  # ← 키 통일

def new(request):
    return render(request, 'garages/new.html')

def create(request):
    if request.method != 'POST':
        return redirect('garages:new')

    location = (request.POST.get('location') or '').strip()

    # capacity 안전 파싱
    capacity_raw = request.POST.get('capacity')
    try:
        capacity = int(capacity_raw) if capacity_raw not in (None, '') else 0
    except ValueError:
        capacity = 0

    ipa_raw = request.POST.get('is_parking_available')
    is_parking_available = ipa_raw in ['True', 'true', '1', 'on']

    opening_time = request.POST.get('opening_time') or ''
    closing_time = request.POST.get('closing_time') or ''

    # 필수값(예: location, opening/closing time) 체크
    if not location or not opening_time or not closing_time:
        return render(request, 'garages/new.html', {
            'error': '위치/영업시간은 필수입니다.'
        })

    Garage.objects.create(
        location=location,
        capacity=capacity,
        is_parking_available=is_parking_available,
        opening_time=opening_time,   # 'HH:MM' 문자열 허용됨
        closing_time=closing_time,   # 비어 있으면 에러 → 위에서 가드
    )
    return redirect('garages:index')
