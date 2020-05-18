from django.urls import path

from hh.views import CategorieView, CompanieView, MainView, VacanciesView, VacancyView

urlpatterns = [
    path('', MainView.as_view()),
    path('vacancies', VacanciesView.as_view()),
    path('vacancies/cat/<str:categorie>', CategorieView.as_view()),
    path('companies/<int:companie_id>', CompanieView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view()),
]
