# Generated by Django 4.2.6 on 2023-10-06 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_salary_job_vacancy_job_experience_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='Salary',
        ),
        migrations.RemoveField(
            model_name='job',
            name='published_at',
        ),
    ]
