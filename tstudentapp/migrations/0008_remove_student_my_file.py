# Generated by Django 3.2.6 on 2021-09-11 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tstudentapp', '0007_student_my_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='my_file',
        ),
    ]
