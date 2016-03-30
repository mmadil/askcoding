# -*- coding: utf-8 -*-

# Third Party
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm

from .models import User


# Forms
# ----------------------------------------------------------------------------
class MyUserCreationForm(DjangoUserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name')


class MyUserChangeForm(DjangoUserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


# ModelAdmins
# ----------------------------------------------------------------------------
@admin.register(User)
class UserAdmin(AuthUserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'receive_emails',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('date_joined', 'last_login')
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'name', 'is_active')
    list_filter = ('is_superuser', 'is_active')
    search_fields = ('name', 'email')
    ordering = ('email',)
