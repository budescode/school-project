from django.shortcuts import render
# from administrator.models import News
from django.shortcuts import render, get_object_or_404, redirect
from administrator.forms import StudentForm, ItForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.models import User
from administrator.models import Student
from django.contrib import messages
from administrator.models import It, Student
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
	return render(request, 'index.html', {})
def about(request):
	return render(request, 'about.html', {})
def contact(request):
	return render(request, 'contact.html', {})

def login_page(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username  = form.cleaned_data.get("username")
			password  = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
			 	if user.is_active:
			 		login(request, user)
			 		return redirect('index:index')
			 	else:
			 		return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	context = {"form": form}
	return render(request, "login.html", context)

def register_it(request):
	if request.method == 'POST':
		form = ItForm(request.POST or None, request.FILES or None)		
		if form.is_valid():
    		
			full_name = request.POST.get("full_name")
			Matriculation_Number = request.POST.get("Matriculation_Number")
			form.save()	
			messages.success(request, Matriculation_Number +  'is successfully Registered')
			context={}
			return render(request, "register_it_success.html", context)
			# return redirect('index:register_it')
	else:
		form = ItForm(request.POST or None) 
	context = {"form": form} 
	return render(request, "register_it.html", context)

def logout_page(request):
	logout(request)
	return redirect('administrator:logged_out')
	
def logged_out(request):
	return render(request, "logout.html", {})


def add_student(request):
	print('entered')
	if request.method == 'POST':
		form = StudentForm(request.POST or None, request.FILES or None)		
		if form.is_valid():    		
			first_name = request.POST.get("first_name")
			last_name = request.POST.get("last_name")
			Matriculation_Number = form.cleaned_data.get("Matriculation_Number")
			department = request.POST.get("department")
			Faculty = request.POST.get("Faculty")
			Level = request.POST.get("Level")
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			print(Level, password, Matriculation_Number, email)
			form.save()
			User.objects.create_user(username=Matriculation_Number, email=email, password=password)
			messages.success(request, Matriculation_Number +  'is successfully Registered')
			return redirect('index:login')
	else:
		form = StudentForm(request.POST or None) 
	context = {"form": form} 
	return render(request, "administrator/register.html", context)


def placement(request):
	qs = It.objects.get(Matriculation_Number=request.user.username)
	context={"qs":qs}
	return render(request, 'placement.html', context)

def progress_sheet(request):
	return render(request, 'progress.html')

def student_details(request):
	qs = Student.objects.get(Matriculation_Number=request.user.username)
	return render(request, 'student.html', {"qs":qs})
