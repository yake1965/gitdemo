from django import forms

class StudentForm(forms.Form):
    sn = forms.CharField(label="学号", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Student number",'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))

class TeacherForm(forms.Form):
    sn = forms.CharField(label="教工号", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Faculty number",'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))

class RegisterForm(forms.Form):
   
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    DEPT = (('信息工程学院','信息工程学院'),)
    MAJOR =(
        ('计算机网络技术','计算机网络技术'),
        ('计算机应用技术','计算机应用技术'),
        ('软件技术','软件技术'),
        ('云计算技术与应用','云计算技术与应用'),
        ('大数据技术与应用','大数据技术与应用'),
        ('网络安全与管理','网络安全与管理'),
        ('电子信息工程技术','电子信息工程技术'),
        )

    id = forms.CharField(label="学号", max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    dept = forms.ChoiceField(label='学院', choices=DEPT)
    major = forms.ChoiceField(label='专业', choices=MAJOR)
    sex = forms.ChoiceField(label='性别', choices=gender)
    birth =forms.DateField(label='出生日期')
    telephone = forms.CharField(label='电话')
               

          
    
   
