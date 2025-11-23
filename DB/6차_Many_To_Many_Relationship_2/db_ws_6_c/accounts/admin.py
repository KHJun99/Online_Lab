from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    # ManyToManyField를 보기 좋게 표시
    filter_horizontal = UserAdmin.filter_horizontal + ('subscription',)
    
    # fieldsets에 구독 정보 추가
    fieldsets = UserAdmin.fieldsets + (
        ('Subscription', {'fields': ('subscription',)}),
    )

admin.site.register(User, CustomUserAdmin)