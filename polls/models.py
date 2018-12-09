from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    q = models.CharField(max_length=200,default='ass')
    question_text = models.CharField(max_length=200)
    question_course = models.CharField(max_length = 200,default = 'dfasdfksaof')
    
    pub_date = models.DateTimeField(auto_now_add=True,null = True)
    def __str__(self):
        return self.question_text
   
class Answer(models.Model):
	question=models.ForeignKey(Question,on_delete=models.SET_NULL, null=True)
	answer_id = models.IntegerField(default = '0',null = True)
	answer = models.CharField(max_length=200,default = 'venkatesh')
	a = models.CharField(max_length=200,default='dhd')
	#extra = models.IntegerField(primary_key=True,default='0')
	aub_date = models.DateTimeField(auto_now_add=True,null = True)
	def __str__(self):
        	return self.answer



class Student(models.Model):
	student_id=models.CharField(primary_key=True,max_length=255)
	student_name=models.CharField(max_length=50,default='')
	middle_name=models.CharField(max_length=50,default='')
	last_name=models.CharField(max_length=50,default='')
	gender=models.CharField(max_length=1,default='m')
	current_year=models.CharField(max_length=3,default='')
	student_email=models.EmailField(default='')
	def __str__(self):
        	return self.student_id
    




class Review(models.Model):
	answer_key=models.ForeignKey(Answer,on_delete=models.SET_NULL, null=True)
	review_id = models.AutoField(primary_key=True)
	avg_review = models.IntegerField(default = '0')
	def __str__(self):
        	return str(self.avg_review)

class Courses(models.Model):
	course_name = models.CharField(max_length=200,default = 'venkatesh')
	course_id = models.IntegerField(default = '0')
	course_faculty = models.CharField(max_length =200,default = 'venkatesh')
	def __str__(self):
        	return self.course_name

class Faculty(models.Model):
	course=models.ForeignKey(Courses,on_delete=models.SET_NULL, null=True)
	faculty_id = models.CharField(primary_key=True,max_length=20)
	faculty_name = models.CharField(max_length = 200,default = 'venkatesh')
	faculty_email = models.EmailField(max_length = 200,default = 'venkatesh')
	def __str__(self):
        	return self.faculty_id





class Login(models.Model):
	username = models.CharField(max_length = 25,default = 'venkatesh')
	password = models.CharField(max_length = 25,default = 'venkatesh')
	email = models.EmailField(max_length = 25,default = 'venkatesh2')
	def __str__(self):
        	return self.username


