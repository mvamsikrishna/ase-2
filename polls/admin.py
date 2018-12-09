from django.contrib import admin

from .models import Question,Answer,Faculty,Student,Review,Courses,Login







admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Review)
admin.site.register(Login)
admin.site.register(Courses)

