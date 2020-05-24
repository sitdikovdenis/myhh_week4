from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from hh import models
from myhh.settings import MEDIA_ROOT
from hh.forms import ApplicationForm, CompanyEditForm, MyAuthenticationForm, SignUpForm


def get_previous_page(request):
    prev_page = request.META.get('HTTP_REFERER')
    if prev_page is None:
        prev_page = '/'
    return prev_page


# Create your views here.
class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'hh/index.html',
            context={"specialty": models.Specialty.objects.all(),
                     "company": models.Company.objects.all(),
                     }
        )


class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'hh/vacancies.html',
            context={"specialty": models.Specialty.objects.all()}
        )


class CategorieView(View):
    def get(self, request, categorie, *args, **kwargs):
        return render(
            request, 'hh/vacancies.html',
            context={"specialty": models.Specialty.objects.filter(code=categorie)}
        )


class CompanieView(View):
    def get(self, request, companie_id, *args, **kwargs):
        return render(
            request, 'hh/company.html',
            context={"company": models.Company.objects.get(id=companie_id),
                     'prev_page': get_previous_page(request)}
        )


class VacancyView(View):
    def get(self, request, vacancy_id, *args, **kwargs):
        if len(models.Vacancy.objects.filter(id=vacancy_id)) == 0:
            raise Http404
        username = "" if not request.user.is_authenticated else ' '.join(
            [request.user.first_name, request.user.last_name])
        form_class = ApplicationForm(initial={'username': username})

        return render(
            request, 'hh/vacancy.html',
            context={'prev_page': get_previous_page(request),
                     "vacancy": models.Vacancy.objects.get(id=vacancy_id),
                     "app_form": form_class}
        )


class ApplicationSendView(View):
    def post(self, request, vacancy_id, *args, **kwargs):
        app_form = ApplicationForm(request.POST)
        if app_form.is_valid():
            data = app_form.cleaned_data
            models.Application.objects.create(written_username=data['username'],
                                              written_phone=data['phone'],
                                              written_cover_letter=data['cover_letter'],
                                              user=request.user,
                                              vacancy=models.Vacancy.objects.get(id=vacancy_id))

            return HttpResponseRedirect(request.path)

    def get(self, request, vacancy_id, *args, **kwargs):
        return render(
            request, 'hh/sent.html',
            context={'prev_page': get_previous_page(request),
                     'title': 'Отклик отправлен | Джуманджи'}
        )


class MyCompanyView(View):
    def get(self, request, *args, **kwargs):
        # search my company
        # if not found, then create, else edit
        my_company_qs = models.Company.objects.filter(owner=request.user)
        if len(my_company_qs) == 0:
            return render(
                request, 'hh/company-create.html',
                context={'title': 'Создать карточку компании | Джуманджи'}
            )
        else:
            my_company_list = list(my_company_qs.values())[0]
            print(my_company_list)
            return render(
                request, 'hh/company-edit.html',
                context={'title': 'Моя компания | Джуманджи',
                         'form': CompanyEditForm(instance=my_company_qs.first()
                                                 )}
            )

    def post(self, request, *args, **kwargs):
        my_company_qs = models.Company.objects.filter(owner=request.user)
        company_form = CompanyEditForm(request.POST, request.FILES)

        if company_form.is_valid():
            company_form.logo = company_form.cleaned_data['logo']
            if len(my_company_qs) == 0:
                company_form.save()
            else:
                company = my_company_qs.first()
                company_form = CompanyEditForm(request.POST, request.FILES, instance=company)
                company_form.save()

            return HttpResponseRedirect(request.path)
        else:
            print(company_form.errors)
            return render(
                request, 'hh/company-edit.html',
                context={'title': 'Моя компания | Джуманджи',
                         'form': CompanyEditForm(initial={'owner': request.user})}
        )


class MyVacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'hh/vacancy-list.html',
            context={}
        )


class MyVacancieView(View):
    def get(self, request, vacancy_id, *args, **kwargs):
        return render(
            request, 'hh/vacancy-list.html',
            context={}
        )


class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'hh/login.html'
    form_class = MyAuthenticationForm


class MySignupView(CreateView):
    form_class = SignUpForm
    success_url = 'login'
    template_name = 'hh/register.html'
