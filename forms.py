from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Locale, Section, Subsection
from classifieds.models import Classified

class CreateClassifiedForm(ModelForm):
    class Meta:
        model = Classified
        fields = ['classified_title', 'classified_text', 'locale', 'section', 'subsection']
