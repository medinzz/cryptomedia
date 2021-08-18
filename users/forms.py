from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserRegistrationForm(UserCreationForm):

	class Meta:
		model = User
		fields = '__all__'


class UserUpdateForm(UserChangeForm):
	class Meta:
		model = User
		fields = '__all__'

