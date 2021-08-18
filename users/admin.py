from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegistrationForm, UserUpdateForm
from .models import User


class UserAdmin(UserAdmin):
	add_form = UserRegistrationForm
	form = UserUpdateForm
	model = User
	list_display = (
		'username',
		'email',
		'first_name',
		'last_name',
		'is_staff',
		'is_active',
		)
	list_filter = (
		'is_staff',
		'is_superuser',
		'is_active',
		)
	fieldsets = (
		(None, {'fields': (
					'username',
					'email',
					'first_name',
					'last_name',
					'password'
					)
				}
			),
		('Permissions',
			{'fields': (
					'is_staff',
					'is_superuser',
					'is_active',
					)
				}
			),
	)
	add_fieldsets = (
		(None, {'classes': ('wide',),
			'fields': (
				'username',
				'email',
				'first_name',
				'last_name',
				'password1',
				'password2',
				'is_staff',
				'is_superuser',
				'is_active',
				)
			}
		),
	)
	search_fields = ('username',)
	ordering = ( 'username',)
admin.site.register(User, UserAdmin)
