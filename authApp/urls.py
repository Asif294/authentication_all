from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.register,name='register'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('profile/',views.profile,name='profile'),
    path('change_pass/',views.change_pass,name='change_pass'),
    path('change_pass_with_old_pass/',views.pass_change2,name='pass_change2'),
    path('profileUpdate/',views.profileUpdate,name='profileUpdate'),
    path('user_logout/',views.user_logout,name='user_logout'),
   

]