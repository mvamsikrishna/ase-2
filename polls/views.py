from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import  Question,Answer,Student
import json
import requests

def signin(request):
	return render(request,'polls/login.html')

def login(request,token):
	global global_studentid
	global global_studentname
	#res = requests.post(url='https://serene-wildwood-35121.herokuapp.com/oauth/getDetails', data={
    #'token': token,
    #'secret': 'eb130fdfd5b678fdd19e4f2c8ab7e4bace85927a538caa34b7a7efb6ddc2f65b0c086bc3753abfe7c726c2e60e651a52a2995d596088de2d364e61e40453a504'
	#})
	res={'token': token,'secret': "eb130fdfd5b678fdd19e4f2c8ab7e4bace85927a538caa34b7a7efb6ddc2f65b0c086bc3753abfe7c726c2e60e651a52a2995d596088de2d364e61e40453a504"}
	url="https://serene-wildwood-35121.herokuapp.com/oauth/getDetails"
	#print(res.content.decode('utf-8'))
	#res = json.loads(res.content.decode('utf-8'))
	#email = res["student"][0]["Student_Email"]
	#st_id = res["student"][0]["Student_ID"]
	#print(email)
	#print(st_id)
	response=requests.post(url,data=res)
	data=response.json()
	print(data)
	email = data["student"][0]["Student_Email"]
	print(email)
	#if(email):
		#return render(request,'polls/index.html')
	stu=Student.objects.all().filter(student_id=data['student'][0]['Student_ID'])
	context = { 'stude_objs' : stu }
	if len(stu)!=0:
		global_studentid=data['student'][0]['Student_ID']

		global_studentname=data['student'][0]['Student_First_Name']

		
	else:
		global_studentid=data['student'][0]['Student_ID']
		global_studentname=data['student'][0]['Student_First_Name']
		student_obj=Student()
		student_obj.student_id=data['student'][0]['Student_ID']
		
		student_obj.student_name=data['student'][0]['Student_First_Name']
		student_obj.last_name=data['student'][0]['Student_Last_name']
		student_obj.middle_name=data['student'][0]['Student_Middle_Name']
		student_obj.gender=data['student'][0]['Student_Gender']
		student_obj.student_email=data['student'][0]['Student_Email']
		student_obj.current_year=data['student'][0]['Student_Cur_YearofStudy']
		student_obj.save()
	return render(request,'polls/index.html',context)

def users(request):
	stud = Student.objects.all().filter(student_id=global_studentid)
	context = { 'student_objs' : Student.objects.all() , 'stud_objs' : stud }
	#print(context)
	
	return render(request,'polls/users.html',context)

def profile(request):
	stude = Student.objects.all().filter(student_id=global_studentid)
	context = { 'stude_objs' : stude }
	return render(request,'polls/profile.html',context)

def index(request):
	st = Student.objects.all().filter(student_id=global_studentid)
	context = { 'st_objs' : st }
	return render(request,'polls/index.html',context)

def courses(request):
	st = Student.objects.all().filter(student_id=global_studentid)
	context = { 'st_objs' : st }
	return render(request,'polls/courses.html',context)


def details(request):
	stud = Student.objects.all().filter(student_id=global_studentid)
	context = { 'student_objs' : Student.objects.all() , 'stud_objs' : stud }
	return render(request,'polls/details.html',context)


def trendingquestions(request):
	if request.method=='POST':
		if request.POST['guess'] == 'search':
			obj = Question.objects.all()
			str1 = request.POST['abcd']
			search_ids = []
			for i in obj:
				a = i.question_text
				lista  = a.split()
				for j in lista:
					if(str1 == j):
						search_ids.append(i.question_id)
						break
			objs = []
			for i in search_ids:
				objs.append(Question.objects.all().filter(question_id = i))
			context = {'question_objs' : objs ,'answer_objs': Answer.objects.all()}
			return render(request,'polls/trendingquestions.html',context )

		if request.POST['guess'] == 'answer':
			print(request.POST['answ'])
			ans = Answer()
			ans.answer = request.POST['answ']
			ans.a = global_studentname
			q = Question.objects.all()
			val = request.POST['write']
			
			for i in q:
				if i.question_text == val:
					ans.answer_id = i.question_id
					break
			#ans.answer_id = 45
			#ans.answer = request.POST['answer']
			ans.save()
	
	#vacancies=Question.objects.all()
	#context={"vacancies":vacancies}
	#return render(request,'vacancies.html', context)
		return render(request,'polls/trendingquestions.html')
	else:
		st = Student.objects.all().filter(student_id=global_studentid)
		context = {'question_objs' : Question.objects.all().order_by('-pub_date') , 'answer_objs':Answer.objects.all().order_by('-aub_date') , 'st_objs' : st}
		return render(request,'polls/trendingquestions.html',context)
		




def digi(request):
	st = Student.objects.all().filter(student_id=global_studentid)
	context = { 'st_objs' : st }
	return render(request,'polls/digi.html',context)

def ls(request):
	st = Student.objects.all().filter(student_id=global_studentid)
	context = { 'st_objs' : st }
	return render(request,'polls/LS.html',context)

def vlsi(request):
	st = Student.objects.all().filter(student_id=global_studentid)
	context = { 'st_objs' : st }
	return render(request,'polls/vlsi.html',context)

def dsp(request):
	st = Student.objects.all().filter(student_id=global_studentid)
	context = { 'st_objs' : st }
	return render(request,'polls/dsp.html',context)



def selectedtopic(request):
	st = Student.objects.all().filter(student_id=global_studentid)
	context = { 'st_objs' : st }
	return render(request,'polls/selectedtopic.html',context)

def selectedtopic1(request):
	st = Student.objects.all().filter(student_id=global_studentid)
	context = { 'st_objs' : st }
	return render(request,'polls/selectedtopic1.html',context)

def selectedtopic2(request):
	st = Student.objects.all().filter(student_id=global_studentid)
	context = { 'st_objs' : st }
	return render(request,'polls/selectedtopic2.html',context)

def selectedtopic3(request):
	st = Student.objects.all().filter(student_id=global_studentid)
	context = { 'st_objs' : st }
	return render(request,'polls/selectedtopic3.html',context)


def viewqa(request):
	if request.method=='POST':
		print(request.POST['guess'])
		if request.POST['guess'] == 'question':

			vac= Question()
			#vac.question_id=request.POST['question_id']
			vac.question_course = request.POST['course1']
			vac.question_text=request.POST['question_text']
			vac.q = global_studentname
			
			vac.save()
		if request.POST['guess'] == 'answer':
			print(request.POST['answ'])
			ans = Answer()
			ans.answer = request.POST['answ']
			ans.a = global_studentname
			q = Question.objects.all()
			val = request.POST['write']
			
			for i in q:
				if i.question_text == val:
					ans.answer_id = i.question_id
					break
			#ans.answer_id = 45
			#ans.answer = request.POST['answer']
			ans.save()
	
	#vacancies=Question.objects.all()
	#context={"vacancies":vacancies}
	#return render(request,'vacancies.html', context)
		return render(request,'polls/viewqa.html')
	else:
		st = Student.objects.all().filter(student_id=global_studentid)
		stu = Student.objects.all().filter(student_id=global_studentname)
		context = {'question_objs' : Question.objects.all().order_by('-pub_date') , 'answer_objs':Answer.objects.all().order_by('-aub_date') , 'st_objs' : st , 'stu_objs' : stu}
		return render(request,'polls/viewqa.html',context)
		
def viewqa1(request):
	if request.method=='POST':
		print(request.POST['guess'])
		if request.POST['guess'] == 'question':

			vac= Question()
			#vac.question_id=request.POST['question_id']
			vac.question_course = request.POST['course2']
			vac.question_text=request.POST['question_text']
			vac.q = global_studentname
			#vac.technical_skills=request.POST['pub_date']
			#vac.other_skills=request.POST['other_skills']
			#vac.expected_salary=request.POST['expected_salary']
			vac.save()
		if request.POST['guess'] == 'answer':
			print(request.POST['answ'])
			ans = Answer()
			ans.answer = request.POST['answ']
			ans.a = global_studentname
			q = Question.objects.all()
			val = request.POST['write']
			
			for i in q:
				if i.question_text == val:
					ans.answer_id = i.question_id
					break
			#ans.answer_id = 45
			#ans.answer = request.POST['answer']
			ans.save()
	
	#vacancies=Question.objects.all()
	#context={"vacancies":vacancies}
	#return render(request,'vacancies.html', context)
		return render(request,'polls/viewqa1.html')
	else:
		st = Student.objects.all().filter(student_id=global_studentid)
		context = {'question_objs' : Question.objects.all().order_by('-pub_date') , 'answer_objs':Answer.objects.all().order_by('-aub_date') , 'st_objs' : st}
		return render(request,'polls/viewqa1.html',context)
		
def viewqa2(request):
	if request.method=='POST':
		print(request.POST['guess'])
		if request.POST['guess'] == 'question':

			vac= Question()
			#vac.question_id=request.POST['question_id']
			vac.question_course = request.POST['course3']
			vac.question_text=request.POST['question_text']
			vac.q = global_studentname
			#vac.technical_skills=request.POST['pub_date']
			#vac.other_skills=request.POST['other_skills']
			#vac.expected_salary=request.POST['expected_salary']
			vac.save()
		if request.POST['guess'] == 'answer':
			print(request.POST['answ'])
			ans = Answer()
			ans.answer = request.POST['answ']
			ans.a = global_studentname
			q = Question.objects.all()
			val = request.POST['write']
			
			for i in q:
				if i.question_text == val:
					ans.answer_id = i.question_id
					break
			#ans.answer_id = 45
			#ans.answer = request.POST['answer']
			ans.save()
	
	#vacancies=Question.objects.all()
	#context={"vacancies":vacancies}
	#return render(request,'vacancies.html', context)
		return render(request,'polls/viewqa2.html')
	else:
		st = Student.objects.all().filter(student_id=global_studentid)
		context = {'question_objs' : Question.objects.all().order_by('-pub_date') , 'answer_objs':Answer.objects.all().order_by('-aub_date') , 'st_objs' : st}
		return render(request,'polls/viewqa2.html',context)
		



def viewqa3(request):
	if request.method=='POST':
		print(request.POST['guess'])
		if request.POST['guess'] == 'question':

			vac= Question()
			#vac.question_id=request.POST['question_id']
			vac.question_course = request.POST['course4']
			vac.question_text=request.POST['question_text']
			vac.q = global_studentname
			#vac.technical_skills=request.POST['pub_date']
			#vac.other_skills=request.POST['other_skills']
			#vac.expected_salary=request.POST['expected_salary']
			vac.save()
		if request.POST['guess'] == 'answer':
			print(request.POST['answ'])
			ans = Answer()
			ans.answer = request.POST['answ']
			ans.a = global_studentname
			q = Question.objects.all()
			val = request.POST['write']
			
			for i in q:
				if i.question_text == val:
					ans.answer_id = i.question_id
					break
			#ans.answer_id = 45
			#ans.answer = request.POST['answer']
			ans.save()
	
	#vacancies=Question.objects.all()
	#context={"vacancies":vacancies}
	#return render(request,'vacancies.html', context)
		return render(request,'polls/viewqa3.html')
	else:
		st = Student.objects.all().filter(student_id=global_studentid)
		context = {'question_objs' : Question.objects.all().order_by('-pub_date') , 'answer_objs':Answer.objects.all().order_by('-aub_date') , 'st_objs' : st}
		return render(request,'polls/viewqa3.html',context)
		

def myquestions(request):
	qu = Question.objects.all().filter(q = global_studentname)
	context = { 'qu_objs' : qu }
	return render(request,'polls/myquestions.html',context)



