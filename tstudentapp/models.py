from django.db import models

# Create your models here.

class Student(models.Model):
    student_name=models.CharField(max_length=50)
    student_fathername=models.CharField(max_length=40,null=True,blank=True)
    student_img=models.ImageField(upload_to="tstudentapp/img")
    student_branch=models.CharField(max_length=40,null=True,blank=True)
    student_age=models.IntegerField(null=True,blank=True)
    student_tenth = models.IntegerField(blank=True,default=0)
    student_twelth=models.IntegerField(null=True,blank=True)
    student_diploma=models.IntegerField(null=True,blank=True)
    student_btech=models.IntegerField(null=True,blank=True)
    student_hobbie=models.CharField(max_length=100,null=True,blank=True)
    technical_skills=models.CharField(max_length=100,null=True,blank=True)
    personal_skills=models.CharField(max_length=100,null=True,blank=True)
    student_achievement=models.CharField(max_length=100,null=True,blank=True)
    student_address=models.CharField(max_length=100,null=True,blank=True)
    student_phone=models.IntegerField(null=True,blank=True)
    student_email=models.CharField(max_length=100,null=True,blank=True)
    student_project1=models.CharField(max_length=100,null=True,blank=True)
    student_project2=models.CharField(max_length=100,null=True,blank=True)
    student_project_skills=models.CharField(max_length=100,null=True,blank=True)
    student_tenth_schoolname=models.CharField(max_length=100,null=True,blank=True)
    student_twelth_diploma_collegename=models.CharField(max_length=100,null=True,blank=True)
    student_current_collegename=models.CharField(max_length=100,null=True,blank=True)
    student_dob=models.DateField(null=True,blank=True)
    student_profile=models.CharField(max_length=300,null=True,blank=True)


    

    def __str__(self):
        return self.student_name


class User(models.Model):
    user=models.TextField(default=None)

    def __str__(self):
        return self.user
    
