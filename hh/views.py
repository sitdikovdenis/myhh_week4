from django.shortcuts import render
from django.views import View

from hh import models


# Create your views here.
class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'hh/index.html',
            context={"specialty": models.Specialty.objects.all(),
                     "company": models.Company.objects.all()}
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
        prev_page = request.META.get('HTTP_REFERER')
        if prev_page is None:
            prev_page = '/'
        return render(
            request, 'hh/company.html',
            context={"company": models.Company.objects.get(id=companie_id),
                     'prev_page': prev_page}
        )


class VacancyView(View):
    def get(self, request, vacancy_id, *args, **kwargs):
        prev_page = request.META.get('HTTP_REFERER')
        if prev_page is None:
            prev_page = '/'
        return render(
            request, 'hh/vacancy.html',
            context={'prev_page': prev_page,
                     "vacancy": models.Vacancy.objects.get(id=vacancy_id)}
        )
