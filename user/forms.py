from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User
from main.models import List

class RegisterForm(forms.ModelForm):
    
    password = forms.CharField(label = 'Mật khẩu',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username','email','fullName')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.object.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Tên đăng nhập đã được sử dụng,vui lòng dùng tên đăng nhập khác")
        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.object.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email đã được sử dụnng")
        return email
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Mật Khẩu Không trùng khớp")
        return password2
    def save(self):
        username = self.cleaned_data['username']
        User.object.create_user(username=username, email=self.cleaned_data['email'], fullName=self.cleaned_data['fullName'] ,password=self.cleaned_data['password2'])
        List.objects.create(user_id = User.object.get(username = username).id)

class LoginForm(forms.ModelForm):
    
    password = forms.CharField(label = 'Mật khẩu',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username',)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.object.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Tên đăng nhập đã được sử dụng,vui lòng dùng tên đăng nhập khác")
        return username
