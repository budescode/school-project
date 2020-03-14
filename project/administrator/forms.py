from django import forms
from .models import Student, It
from ckeditor.widgets import CKEditorWidget
#from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget


class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['first_name', 'last_name', 'email', 'Matriculation_Number', 'department', 'Faculty', 'Level',  'password']

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput( 
		attrs={'class':'form-control', 'placeholder':'Enter username'}))
	password = forms.CharField(widget=forms.PasswordInput( 
		attrs={'class':'form-control', 'placeholder':'Enter Password'}))

class ItForm(forms.ModelForm):
	class Meta:
		model = It
		fields = ['full_name', 'Matriculation_Number', 'course_of_study', 'Faculty', 'Level',  'name_of_the_company', 'address_of_the_company', 'department', 'name_of_industry_based_supervisor', 'address_of_industry_based_supervisor']