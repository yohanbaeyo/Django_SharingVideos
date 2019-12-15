from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    verify_password = forms.CharField(label="비밀번호 확인",
                                      widget= forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호 확인'}
            ))
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'verify_password']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '아이디'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': '이메일'}
            ),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': '비밀번호'}
            ),
        }

    def clean_verify_password(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['verify_password']
        if password1 != password2:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '아이디'}
            ),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': '비밀번호'}
            ),
        }

