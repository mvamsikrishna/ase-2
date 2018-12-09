import json
import requests
from django.conf.urls import include,url
from django.shortcuts import get_object_or_404, render
from polls.models import *
def login(request,token):
	global global_studentid
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
	if len(stu)!=0:
		global_studentid=data['student'][0]['Student_ID']
		
	else:
		student_obj=Student()
		student_obj.student_id=data['student'][0]['Student_ID']
		global_studentid=data['student'][0]['Student_ID']
		student_obj.student_name=data['student'][0]['Student_First_Name']
		student_obj.last_name=data['student'][0]['Student_Last_name']
		student_obj.middle_name=data['student'][0]['Student_Middle_Name']
		student_obj.gender=data['student'][0]['Student_Gender']
		student_obj.student_email=data['student'][0]['Student_Email']
		student_obj.current_year=data['student'][0]['Student_Cur_YearofStudy']
		student_obj.save()
	return render(request,'polls/index.html')