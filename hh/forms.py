from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from hh import models


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(label='Фамилия', max_length=30, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)


class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password',)


class ApplicationForm(forms.Form):
    username = forms.CharField(label='Вас зовут', max_length=64, min_length=2,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    phone = forms.CharField(max_length=50, label='Ваш телефон',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    cover_letter = forms.CharField(max_length=8000, label='Сопроводительное письмо',
                                   widget=forms.Textarea(attrs={'class': 'form-control'}))


class CompanyEditForm2(forms.Form):
    name = forms.CharField(label='Название компании', max_length=256, min_length=2,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    logo = forms.ImageField(label='Логотип',
                            )

    employee_count = forms.CharField(max_length=20, label='Количество человек в компании',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))

    location = forms.CharField(max_length=256, label='География',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    description = forms.CharField(max_length=4096, label='Информация о компании',
                                  widget=forms.Textarea(attrs={'class': 'form-control'}))


class CompanyEditForm(ModelForm):
    logo = forms.ImageField(allow_empty_file=True, required=False)

    class Meta:
        model = models.Company
        fields = ['name', 'logo', 'employee_count', 'location', 'description', 'owner']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_count': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'owner': forms.Textarea(attrs={'class': 'form-control'}),

        }
        labels = {
            'name': 'Название компании',
            'employee_count': 'Количество человек в компании',
            'location': 'География',
            'description': 'Информация о компании',
            'logo': 'Логотип',
            'owner': 'Владелец'
        }
