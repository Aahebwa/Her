from . import models
from django import forms

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = models.UploadFile
        fields = ['file_title', 'file']

class CreateCourseUnit(forms.ModelForm):
    class Meta:
        model = models.Course_unit
        fields = ['unit_title', 'course_code','slug', 'unit_description']
