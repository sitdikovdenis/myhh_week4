import datetime
import re
from functools import reduce

from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from hh import models
from hh.forms import ApplicationForm, CompanyEditForm, MyAuthenticationForm, SignUpForm, VacancyEditForm, ResumeEditForm


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
        if len(models.Company.objects.filter(id=companie_id)) == 0:
            raise Http404
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

        application_form = ApplicationForm(request.POST, request.FILES)

        if application_form.is_valid():
            application = application_form.save(commit=False)
            application.user = request.user
            application.vacancy = models.Vacancy.objects.get(id=vacancy_id)
            application.save()
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
            # здесь мы сохраняем новую или существующую компанию
            if len(my_company_qs) == 0:
                company = company_form.save(commit=False)
                company.owner = request.user
                company.save()
            else:
                company = my_company_qs.first()
                company_form = CompanyEditForm(request.POST, request.FILES, instance=company)
                company_form.save()

            return HttpResponseRedirect(request.path, )
        else:
            # сюда мы попадем, если нажмем создать компанию
            return render(
                request, 'hh/company-edit.html',
                context={'title': 'Моя компания | Джуманджи',
                         'form': CompanyEditForm(initial={'owner': request.user})}
            )


# вакансии моей компании
class MyCompanyVacanciesView(View):
    def get(self, request, *args, **kwargs):
        my_company_qs = models.Company.objects.filter(owner=request.user)
        if len(my_company_qs) == 0:
            return HttpResponseRedirect("/mycompany")
        else:
            my_company = my_company_qs.first()
            vacancies = models.Vacancy.objects.filter(company=my_company)
            return render(
                request, 'hh/vacancy-list.html',
                context={
                    'title': 'Вакансии компании | Джуманджи',
                    'form': CompanyEditForm(instance=my_company_qs.first()),
                    'vacancies': vacancies
                }
            )


# одна конкретная вакансия моей компании
class MyVacancieView(View):
    def get(self, request, vacancy_id, *args, **kwargs):
        vacancy_qs = models.Vacancy.objects.filter(id=int(vacancy_id), company__owner=request.user)
        if len(vacancy_qs) == 0:
            raise Http404
        else:
            applications = models.Application.objects.filter(vacancy=vacancy_qs.first())
            return render(
                request, 'hh/vacancy-edit.html',
                context={'title': 'Вакансии компании | Джуманджи',
                         'form': VacancyEditForm(instance=vacancy_qs.first()),
                         'applications': applications}
            )

    def post(self, request, vacancy_id, *args, **kwargs):
        my_company_qs = models.Company.objects.filter(owner=request.user)
        #  считаем, что на эту страницу можно попасть, только если у тебя есть компания
        my_company = my_company_qs.first()
        if vacancy_id == "create":
            vacancy_form = VacancyEditForm(request.POST, )

            if vacancy_form.is_valid():
                vacancy = vacancy_form.save(commit=False)
                vacancy.published_at = datetime.datetime.now()
                vacancy.company = my_company
                vacancy.save()
                return HttpResponseRedirect("/mycompany/vacancies/" + str(vacancy.id))
            else:
                pass
            return render(
                request, 'hh/vacancy-edit.html',
                context={'form': VacancyEditForm()}
            )
        else:
            vacancy_qs = models.Vacancy.objects.filter(id=int(vacancy_id))
            vacancy_form = VacancyEditForm(request.POST)

            if vacancy_form.is_valid():
                vacancy = vacancy_qs.first()
                vacancy_form = VacancyEditForm(request.POST, request.FILES, instance=vacancy)
                vacancy = vacancy_form.save()
                vacancy.published_at = datetime.datetime.now()
                vacancy.company = my_company
                vacancy.save()

                return HttpResponseRedirect(request.path)
            else:
                print(vacancy_form.errors)
                return render(
                    request, 'hh/company-edit.html',
                    context={'title': 'Моя компания | Джуманджи',
                             'form': CompanyEditForm()}
                )


class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'hh/login.html'
    form_class = MyAuthenticationForm


class MySignupView(CreateView):
    form_class = SignUpForm
    success_url = 'login'
    template_name = 'hh/register.html'


class SearchView(View):
    def get(self, request, *args, **kwargs):
        question = request.GET.get('q')
        print(question)
        search_context = {}
        if question is not None:
            search_vacancies = models.Vacancy.objects.filter(
                reduce(lambda x, y: x | y, [Q(title__contains=word) for word in re.split(r'\W+', question)]))
            search_context = {'search_vacancies': search_vacancies}
        return render(
            request, 'hh/search.html',
            context=search_context
        )

    def post(self, request, *args, **kwargs):
        question = request.GET.get('q')
        print("qqq " + question)
        return render(
            request, 'hh/search.html',
            context={}
        )


class MyResumeView(View):
    def get(self, request, *args, **kwargs):
        # search my resume
        # if not found, then create, else edit
        my_resume_qs = models.Resume.objects.filter(user=request.user)
        if len(my_resume_qs) == 0:
            return render(
                request, 'hh/resume-create.html',
                context={'title': 'Создать резюме | Джуманджи'}
            )
        else:
            return render(
                request, 'hh/resume-edit.html',
                context={'title': 'Моя компания | Джуманджи',
                         'form': ResumeEditForm(instance=my_resume_qs.first()
                                                )}
            )

    def post(self, request, *args, **kwargs):
        my_resume_qs = models.Resume.objects.filter(user=request.user)
        resume_form = ResumeEditForm(request.POST)

        if resume_form.is_valid():
            # здесь мы сохраняем новую или существующую компанию
            if len(my_resume_qs) == 0:
                resume = resume_form.save(commit=False)
                resume.user = request.user
                resume.save()
                update = False
            else:
                resume = my_resume_qs.first()
                resume_form = ResumeEditForm(request.POST, instance=resume)
                resume_form.save()
                update = True
            return render(
                request, 'hh/resume-edit.html',
                context={'title': 'Мое резюме | Джуманджи',
                         'form': ResumeEditForm(instance=resume),
                         'update': update}
            )
        else:
            # сюда мы попадем, если нажмем создать резюме
            return render(
                request, 'hh/resume-edit.html',
                context={'title': 'Моя компания | Джуманджи',
                         'form': ResumeEditForm(initial={'name': request.user.first_name,
                                                         'surname': request.user.last_name})}
            )
