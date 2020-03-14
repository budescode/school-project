from django.contrib import admin

from .models import Student, It




class StudentAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name','email', 'Matriculation_Number', 'department', 'Faculty', 'Level', 'password']

admin.site.register(Student, StudentAdmin)
admin.site.register(It)
