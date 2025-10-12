from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
   class Meta(UserCreationForm.Meta):
      model = User


class CustomUserChangeForm(UserChangeForm):
    password = None  # 비번 필드는 수정폼에서 숨김
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ("first_name", "last_name")  # ← 두 가지만 수정 가능