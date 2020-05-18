from django.db import models


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.CharField(max_length=256)


class Company(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    logo = models.CharField(max_length=256)
    description = models.CharField(max_length=4096)
    employee_count = models.IntegerField()


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, related_name="vacancies",
                                  on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name="vacancies",
                                on_delete=models.CASCADE)
    skills = models.CharField(max_length=1024)
    description = models.CharField(max_length=8000)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateTimeField()
