from . import views
from django.urls import path 
urlpatterns = [

    path('', views.home,name='home'),
    path('login/', views.loginn,name='login'),
    path('login_out/', views.login_out,name='login_out'),

    path('my_profil/', views.profil,name='profil'),

    path('contact/', views.contact,name='contact'),



    path('signup/', views.sign_up,name='singup'),


    

    
]

