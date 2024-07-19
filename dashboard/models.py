from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course_unit(models.Model):
    unit_title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, null=True)
    slug = models.SlugField(max_length=50, null=False, default="")
    unit_description = models.TextField(max_length=100)
    unit_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.unit_title

class UploadFile(models.Model):
    file_title = models.CharField(max_length=100, default="", null=False)
    file = models.FileField(upload_to='uploads', default="", null=False)
    file_author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.file_title
