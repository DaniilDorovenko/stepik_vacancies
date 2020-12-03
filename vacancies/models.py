from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Company(models.Model):
    title = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.ImageField(upload_to=settings.MEDIA_COMPANY_IMAGE_DIR)
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE)


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.TextField()
    picture = models.ImageField(upload_to=settings.MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    skills = models.CharField(max_length=64)
    description = models.TextField()
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published_at = models.DateTimeField(auto_now_add=True)