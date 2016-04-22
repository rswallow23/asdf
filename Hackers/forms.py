from django import forms
from .models import Posts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
	class Meta:
		model = Posts 
		fields = [
			"title",
			"content",
			"user",
		]
		widgets = {
			"user":forms.HiddenInput()
		}

# class UserForm(UserCreationForm):
# 	class Meta:
# 		model = User 
# 		fields = ['username','password1','password2']