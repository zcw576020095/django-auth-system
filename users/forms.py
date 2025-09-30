from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    """用户注册表单"""
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    """用户登录表单"""
    class Meta:
        model = User
        fields = ['username', 'password']


class UserChangePasswordForm(PasswordChangeForm):
    """用户修改密码表单"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自定义字段属性
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '请输入当前密码'
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '请输入新密码'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '请再次输入新密码'
        })