from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Profile


admin.site.register(get_user_model(), UserAdmin)

class ProfileInline(admin.StackedInline): # 유저 밑에 프로필을 붙여서 보여주려고 상속받음
    model = Profile
    con_delete = False # 프로필을 없앨 수 없게 하는 속성


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# 기존의 User의 등록을 취소했다가 User와 ProfileInline을 붙임.
admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), CustomUserAdmin)