from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from hh.views import ApplicationSendView, CategorieView, CompanieView, LoginView, MainView, MyCompanyView, \
    MyVacancieView, \
    MyVacanciesView, \
    MySignupView, \
    VacanciesView, \
    VacancyView

urlpatterns = [
    path('', MainView.as_view()),
    path('vacancies', VacanciesView.as_view()),
    path('vacancies/cat/<str:categorie>', CategorieView.as_view()),
    path('companies/<int:companie_id>', CompanieView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view()),
    path('admin/', admin.site.urls),
    path('vacancies/<str:vacancy_id>/sent', ApplicationSendView.as_view()),
    path('mycompany', MyCompanyView.as_view()),
    path('mycompany/vacancies', MyVacanciesView.as_view()),
    path('mycompany/vacancies/<int:vacancy_id>', MyVacancieView.as_view()),
    path('login', LoginView.as_view()),
    path('register', MySignupView.as_view(), name="register"),
    path('logout', LogoutView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
