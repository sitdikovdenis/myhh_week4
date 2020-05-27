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


class ApplicationForm(ModelForm):
    class Meta:
        model = models.Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']
        widgets = {
            'written_username': forms.TextInput(attrs={'class': 'form-control'}),
            'written_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'written_cover_letter': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'written_username': 'Вас зовут',
            'written_phone': 'Ваш телефон',
            'written_cover_letter': 'Сопроводительное письмо',
        }


class CompanyEditForm(ModelForm):
    logo = forms.ImageField(allow_empty_file=True, required=False)

    class Meta:
        model = models.Company
        fields = ['name', 'logo', 'employee_count', 'location', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_count': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'owner': forms.Textarea(attrs={'class': 'form-control'}),
            'logo': forms.ImageField(required=True)
        }
        labels = {
            'name': 'Название компании',
            'employee_count': 'Количество человек в компании',
            'location': 'География',
            'description': 'Информация о компании',
            'logo': 'Логотип',
            'owner': 'Владелец'
        }


class VacancyEditForm(ModelForm):
    class Meta:
        model = models.Vacancy
        fields = ['title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'specialty': forms.Select(attrs={'class': 'form-control'}, ),
            'salary_min': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary_max': forms.NumberInput(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class': 'form-control',
                                            'rows': 3,
                                            'style': "color:#000;"}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'rows': 13})

        }
        labels = {
            'title': 'Название вакансии',
            'specialty': 'Специализация',
            'salary_min': 'Зарплата от',
            'salary_max': 'Зарплата до',
            'skills': 'Требуемые навыки',
            'description': 'Описание вакансии',
        }


class ResumeEditForm(ModelForm):
    class Meta:
        model = models.Resume
        fields = ['name', 'surname', 'status', 'salary', 'specialty', 'grade', 'education', 'experience', 'portfolio']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}, ),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'specialty': forms.Select(attrs={'class': 'form-control'}, ),
            'grade': forms.Select(attrs={'class': 'form-control'}, ),
            'education': forms.Textarea(attrs={'class': 'form-control',
                                               'rows': 4,
                                               'style': "color:#000;"}),
            'experience': forms.Textarea(attrs={'class': 'form-control',
                                                'rows': 4,
                                                'style': "color:#000;"}),
            'portfolio': forms.URLInput(attrs={'class': 'form-control',}),

        }
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'status': 'Готовность к работе',
            'salary': 'Ожидаемое вознаграждение',
            'specialty': 'Специализация',
            'grade': 'Квалификация',
            'education': 'Образование',
            'experience': 'Опыт работы',
            'portfolio': 'Ссылка на портфолио',
        }
