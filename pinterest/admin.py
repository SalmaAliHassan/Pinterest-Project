from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.models import Token
from .models import Pin,User,Board,Tag,Section,Note,Notification,Comment,Like


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name')

    fieldsets = (
        ('General Info', {'fields': ('username', 'password'), }),
        ('Personal info', {'fields': ('first_name', 'email','followers')}),

        (None, {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), }),
        (None, {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User,CustomUserAdmin)
admin.site.register(Pin)
admin.site.register(Board)
admin.site.register(Tag)
admin.site.register(Section)
admin.site.register(Note)
admin.site.register(Notification)
admin.site.register(Comment)
admin.site.register(Like)
