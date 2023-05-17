from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Exercise, Program
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

admin.site.register(Exercise)
admin.site.register(Program)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

