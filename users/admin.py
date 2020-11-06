from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from django.contrib.auth import get_user_model

from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = ('username', 'is_staff', 'is_active', 'trading_exp', 'date_joined')
    list_filter = ('username', 'is_staff', 'is_active', 'trading_exp', 'date_joined')
    readonly_fields = ["date_joined"]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'trading_exp')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(get_user_model(), CustomUserAdmin)
