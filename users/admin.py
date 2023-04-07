from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import BadgeUser

CustomUser = get_user_model()


class BadgeUserAdmin(admin.ModelAdmin):
    list_display = ("id","title",)

admin.site.register(BadgeUser, BadgeUserAdmin)

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email', 'username', 'badge']
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Informações Pessoais', {'fields':('first_name', 'last_name', 'bio', 'birth_date', 'perfilIMG','badge')}),
		('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		('Datas importantes', {'fields': ('last_login', 'date_joined')})
	)

admin.site.register(CustomUser, CustomUserAdmin)