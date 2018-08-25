from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
	email = forms.EmailField(max_length=200, help_text='Required')

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name', 
			'email', 
			'password1',
			'password2'
			)

class EditProfileForm(forms.ModelForm):
	email = forms.EmailField(max_length=200, help_text='Required')

	class Meta:
		model = User
		fields = (
			'email',
			'first_name',
			'last_name',
			)
		