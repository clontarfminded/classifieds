from django.db import models
from django.utils import timezone

class Locale(models.Model):
    locale_name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=8)
    province = models.ForeignKey('Province', on_delete=models.CASCADE)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    def __str__(self):
        return self.locale_name

class Sublocale(models.Model):
    sublocale_name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=8)
    province = models.ForeignKey('Province', on_delete=models.CASCADE)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    parent_locale = models.ForeignKey('Locale', on_delete=models.CASCADE)
    def __str__(self):
        return self.abbreviation

class Province(models.Model):
    province_name = models.CharField(max_length=200)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    def __str__(self):
        return self.province_name

class Region(models.Model):
    region_name = models.CharField(max_length=200)
    def __str__(self):
        return self.region_name

class Section(models.Model):
    section_name = models.CharField(max_length=200)
    def __str__(self):
        return self.section_name

class Subsection(models.Model):
    subsection_name = models.CharField(max_length=200)
    def __str__(self):
        return self.subsection_name

class Classified(models.Model):
    classified_title = models.CharField(max_length=200)
    classified_text = models.TextField()
    datetime_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    locale = models.ForeignKey('Locale', on_delete=models.CASCADE)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    subsection = models.ForeignKey('Subsection', on_delete=models.CASCADE)
    def __str__(self):
        return self.classified_title
    def was_created_recently(self):
        return self.datetime_created >= timezone.now() - datetime.timedelta(days=1)

class Page(models.Model):
    page_name = models.CharField(max_length=200)
    page_text = models.TextField()
    def __str__(self):
        return self.page_name
