from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from hh.views import ApplicationSendView, CategorieView, CompanieView, LoginView, MainView, MyCompanyView, \
    MyVacancieView, \
    MyCompanyVacanciesView, \
    MyResumeView, \
    MySignupView, \
    SearchView, \
    VacanciesView, \
    VacancyView

urlpatterns = [
    path('', MainView.as_view()),  # главная
    path('vacancies', VacanciesView.as_view()),
    path('vacancies/cat/<str:categorie>', CategorieView.as_view()),  # вакансии по категории
    path('companies/<int:companie_id>', CompanieView.as_view()),  # компания
    path('vacancies/<int:vacancy_id>', VacancyView.as_view()),  # вакансия
    path('admin/', admin.site.urls),  # админка
    path('vacancies/<str:vacancy_id>/sent', ApplicationSendView.as_view()),  # отпрвка отклика на вакансию
    path('mycompany', MyCompanyView.as_view()),  # моя компания
    path('mycompany/vacancies', MyCompanyVacanciesView.as_view()),  # вакансии моей компании
    path('mycompany/vacancies/<str:vacancy_id>', MyVacancieView.as_view()),  # одна вакансия моей компании
    path('login', LoginView.as_view()),  # логин
    path('register', MySignupView.as_view(), name="register"),  # регистрация
    path('logout', LogoutView.as_view()),  # выход
    path('search', SearchView.as_view()),  # поиск
    path('myresume', MyResumeView.as_view()),  # мое резюме
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
