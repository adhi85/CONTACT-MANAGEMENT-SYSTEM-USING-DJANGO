from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='firstpage'),
     path('home/', views.home, name='home'),
     path('table/', views.table, name='table'),
     path('add/', views.add, name='add'),

     path('profile/<str:pk>', views.contactProfile, name="contact-profile"),
     path('delete-contact/<str:pk>', views.deleteContact , name ="delete-contact"),
     path('allcontacts/', views.allcontacts, name='allcontacts'),

     path('update-contact/<str:pk>', views.updateContact , name ="update-contact"),

     path('register/', views.registerUser , name ="register-user"),
     path('login/', views.loginUser , name ="login-user"),
     path('logout/', views.logoutUser , name ="logout"),

]
