from . import views

from django.urls import path

from administrator import views as GeneratePDF

app_name = "administrator"

urlpatterns = [

	path('', views.administrator, name='administrator'),

	path('register/', views.add_student, name='register'),

	path('login/', views.login_page, name='login'),
	
	path('register_it/', views.register_it, name='register_it'),	

	path('logout/', views.logout_page, name='logout'),

	path('logged_out/', views.logged_out, name='logged_out'),

	path('eligible/', views.eligible_students, name='eligible_students'),





]