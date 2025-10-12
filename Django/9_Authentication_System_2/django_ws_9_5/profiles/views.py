from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


User = get_user_model()

# Create your views here.
@login_required
def index(request):
    persons = User.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'profiles/index.html', context)