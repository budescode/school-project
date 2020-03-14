from django.shortcuts import render

from .models import Student, It

from .forms import StudentForm, ItForm, LoginForm

from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from django.http import HttpResponseRedirect, HttpResponse,JsonResponse

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate, login, get_user_model, logout


@login_required(login_url='/administrator/login/')
def administrator(request):
    return render(request, 'administrator/base.html', {})

def add_student(request):
	if request.method == 'POST':
		form = StudentForm(request.POST or None, request.FILES or None)		
		if form.is_valid():
    		
			first_name = request.POST.get("first_name")
			last_name = request.POST.get("last_name")
			Matriculation_Number = request.POST.get("Matriculation_Number")
			department = request.POST.get("department")
			Faculty = request.POST.get("Faculty")
			Level = request.POST.get("Level")
			email = request.POST.get("email")
			password = request.POST.get("password")
			form.save()
			User.objects.create(username=Matriculation_Number, email=email, password=password)
			# print(first_name, last_name, Matriculation_Number, department, Faculty, Level, email, Phone_Number)
			# ok = form.save(commit = False)
			# print(ok.surname)
			# ok.save()
			print("ok")
			messages.success(request, Matriculation_Number +  'is successfully Registered')

			# add_subject(ok.pk, ok)

			return redirect('administrator:register')
	else:
		form = StudentForm(request.POST or None) 
	context = {"form": form} 
	return render(request, "administrator/register.html", context)


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
			 		return redirect('administrator:administrator')
			 	else:
			 		return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	context = {"form": form}
	return render(request, "administrator/login.html", context)


def register_it(request):
	if request.method == 'POST':
		form = ItForm(request.POST or None, request.FILES or None)		
		if form.is_valid():
    		
			# first_name = request.POST.get("first_name")
			# last_name = request.POST.get("last_name")
			# Matriculation_Number = request.POST.get("Matriculation_Number")
			# department = request.POST.get("department")
			# Faculty = request.POST.get("Faculty")
			# Level = request.POST.get("Level")
			# email = request.POST.get("email")
			# password = request.POST.get("password")
			# form.save()
			# User.objects.create(username=Matriculation_Number, email=email, password=password)
			messages.success(request, Matriculation_Number +  'is successfully Registered')
			return redirect('administrator:register')
	else:
		form = ItForm(request.POST or None) 
	context = {"form": form} 
	return render(request, "administrator/register_it.html", context)

def logout_page(request):
	logout(request)
	return redirect('administrator:logged_out')
	
def logged_out(request):
	return render(request, "administrator/logout.html", {})

def eligible_students(request):
	qs = It.objects.all()

	return render(request, 'administrator/eligible.html', {"qs":qs})