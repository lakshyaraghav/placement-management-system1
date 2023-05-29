from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Student,User
# Register your models here.


class AdminStudent(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','student_name','student_fathername','student_img','student_branch','student_age','student_tenth','student_twelth',
    'student_diploma','student_btech','student_hobbie','technical_skills','personal_skills','student_achievement',
    'student_address','student_phone','student_email','student_profile','student_dob','student_current_collegename',
    'student_twelth_diploma_collegename','student_tenth_schoolname','student_project_skills','student_project1',
    'student_project2']


    

admin.site.register(Student,AdminStudent)
admin.site.register(User)