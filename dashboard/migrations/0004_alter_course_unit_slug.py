# Generated by Django 4.2.11 on 2024-07-09 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_course_unit_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_unit',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
