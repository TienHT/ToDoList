from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class RegisterForm(forms.ModelForm):
    
    password = forms.CharField(label = 'Mật khẩu',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username','email')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.object.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Tên đăng nhập đã được sử dụnng,vui lòng dùng tên đăng nhập khác")
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
            raise forms.ValidationError("Passwords don't match")
        return password2
    def save(self):
        User.object.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password2'])