from . import views

from django.urls import path



app_name = "index"

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),


	path('register/', views.add_student, name='register'),

	path('login/', views.login_page, name='login'),
	
	path('register_it/', views.register_it, name='register_it'),	

	path('logout/', views.logout_page, name='logout'),

	path('logged_out/', views.logged_out, name='logged_out'),

	path('placement/', views.placement, name='placement'),

	path('progress/', views.progress_sheet, name='progress_sheet'),

	path('student/', views.student_details, name='student_details'),






]