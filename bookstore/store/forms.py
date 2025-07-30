from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentFrom(forms.ModelFrom):
    class Meta:
        model = Comment
        fields = ['text', 'rating']
class RegisterFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']