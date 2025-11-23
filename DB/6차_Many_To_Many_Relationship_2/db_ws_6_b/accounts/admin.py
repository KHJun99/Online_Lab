from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # ManyToManyField를 보기 좋게 표시
    filter_horizontal = UserAdmin.filter_horizontal + ('followings',)
       
    # fieldsets에 구독 정보 추가
    fieldsets = UserAdmin.fieldsets + (
        ('Subscription', {'fields': ('followings',)}),
    )

admin.site.register(User, CustomUserAdmin)