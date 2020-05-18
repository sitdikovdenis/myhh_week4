# from hh import data
# from hh import models
#
# for item in data.specialties:
#     specialty = models.Specialty.objects.create(
#         code=item["code"],
#         title=item["title"]
#     )
#
# for item in data.companies:
#     companie = models.Company.objects.create(
#         name=item["title"],
#         location="",
#         logo="",
#         description="",
#         employee_count=0
#     )
#
# for item in data.jobs:
#     company = models.Company.objects.get(name=item["company"])
#     cat = models.Specialty.objects.get(code=item["cat"])
#     vacancy = models.Vacancy.objects.create(
#         title=item["title"],
#         salary_min=item["salary_from"],
#         salary_max=item["salary_to"],
#         description=item["desc"],
#         published_at=item["posted"],
#         specialty=cat,
#         company=company
#     )
#
# specialtys = models.Specialty.objects.distinct()
# print(specialtys)
# for e in models.Vacancy.objects.all():
#     print(e.title)
#
# {"title": "Питонист в стартап", "cat": "backend",
# "company": "primalassault", "salary_from": "120000",
#  "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"}
#
# for item in data.jobs:
#
# models.Vacancy.objects.filter(specialty=models.Specialty.objects.get(code="testing")).delete()
#
# company = models.Company.objects.get(name="workiro")
# cat = models.Specialty.objects.get(code="testing")
# vacancy = models.Vacancy.objects.create(
#     title="QA",
#     salary_min=20000,
#     salary_max=40000,
#     description="QA",
#     published_at="2020-05-11",
#     specialty=cat,
#     company=company
# )
#
# for e in models.Vacancy.objects.all():
#     print(e.title)
