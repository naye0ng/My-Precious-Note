from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, UserChangeForm
from .models import User

class CustomLoginForm(AuthenticationForm) :
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate','placeholder': '아이디'}),label='아이디')

class CustomUserCreationForm(UserCreationForm) :
    class Meta(UserCreationForm.Meta) :
        model = User
        fields = ["username", "nickname"]
        widgets = {
            'username' : forms.TextInput(
                attrs = {
                    'placeholder' : '아이디',
                }
            ),
            'nickname' : forms.TextInput(
                attrs = {
                    'placeholder' : '닉네임',
                }
            )
        }
        labels = {
            'username' :  '아이디',
            'nickname' :  '닉네임',
        }
        help_texts = {
            'nickname' : '닉네임을 입력해주세요.',
        }

class CustomUserChangeForm(UserChangeForm) :
    password = None
    class Meta(UserChangeForm.Meta) :
        model = User
        fields = ["nickname"]
        widgets = {
            'nickname' : forms.TextInput(
                attrs = {
                    'placeholder' : '닉네임',
                }
            )
        }
        labels = {
            'nickname' :  '닉네임',
        }
        help_texts = {
            'nickname' : '변경할 닉네임을 입력해주세요.',
        }

