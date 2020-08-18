from django import forms
from .models import Article, CustomUser, Comment
# from django.contrib.auth.models import User

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content','image']
        
class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','password']
        help_texts = {
            'username': None,
        }
class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','password','nickname','phone_number','grade','major']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']