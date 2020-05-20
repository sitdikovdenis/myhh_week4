from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from hh.views import CategorieView, CompanieView, MainView, VacanciesView, VacancyView

urlpatterns = [
    path('', MainView.as_view()),
    path('vacancies', VacanciesView.as_view()),
    path('vacancies/cat/<str:categorie>', CategorieView.as_view()),
    path('companies/<int:companie_id>', CompanieView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view()),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)