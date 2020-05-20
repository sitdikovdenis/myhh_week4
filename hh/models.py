from django.contrib.auth.models import User
from django.db import models

from myhh.settings import MEDIA_SPECIALITY_IMAGE_DIR, MEDIA_COMPANY_IMAGE_DIR


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR,
                                height_field='height_field',
                                width_field='width_field',
                                default=None,
                                null=True,
                                blank=True)
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)


class Company(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256,
                                default=None,
                                null=True,
                                blank=True)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR,
                             height_field='height_field',
                             width_field='width_field',
                             default=None,
                             null=True
                             )
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=4096,
                                   default=None,
                                   null=True,
                                   blank=True)
    employee_count = models.IntegerField()
    owner = models.ForeignKey(User,
                              related_name="company",
                              on_delete=models.CASCADE,
                              default=None,
                              null=True,
                              blank=True)


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty,
                                  related_name="vacancies",
                                  on_delete=models.CASCADE)

    company = models.ForeignKey(Company,
                                related_name="vacancies",
                                on_delete=models.CASCADE)

    skills = models.CharField(max_length=1024)
    description = models.CharField(max_length=8000)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateTimeField()


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=50)
    written_cover_letter = models.CharField(max_length=8000)

    vacancy = models.ForeignKey(Vacancy,
                                related_name="applications",
                                on_delete=models.CASCADE)

    user = models.ForeignKey(User,
                             related_name="applications",
                             on_delete=models.CASCADE)
