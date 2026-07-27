from django.urls import path

from . import views

 

urlpatterns = [

    path('', views.login, name='login'),
    path('register/',views.register, name='register'),
    path('home/',views.home, name='home'),
    path('logout/',views.logout, name='logout'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('view_patient/', views.view_patient, name='view_patient'),
    path('edit_patient/<int:id>/', views.edit_patient, name='edit_patient'),
    path('delete_patient/<int:id>/',views.delete_patient,name='delete_patient'),
    path('add_doctor/',views.add_doctor, name='add_doctor'),
    path('view_doctor/', views.view_doctor, name= 'view_doctor'),
    path('edit_doctor/<int:id>/', views.edit_doctor, name='edit_doctor'),
    path('delete_doctor/<int:id>/', views.delete_doctor, name='delete_doctor'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('view_appointment/', views.view_appointment, name='view_appointment'),
    path('edit_appointment/<int:id>/', views.edit_appointment, name='edit_appointment'),
    path('delete_appointment/<int:id>/', views.delete_appointment, name='delete_appointment'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('view_medicine/', views.view_medicine, name='view_medicine'),
    path('edit_medicine/<int:id>/', views.edit_medicine, name='edit_medicine'),
    path('delete_medicine/<int:id>/',views.delete_medicine, name='delete_medicine'),

]

