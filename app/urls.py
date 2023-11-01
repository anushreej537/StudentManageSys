from django.urls import path
from app import views
from app.api.api import *
urlpatterns = [
    path('',views.index),
    path('courses/',views.courses),
    path('addcourse/',views.addcourse),
    path('dashboard/',views.dashboard),
    path('signup/',views.signup),
    path('registration/',views.registration),
    path('login_user/',views.login),
    path('addstudent/',views.addstudent),
    path('studentdetails/',views.studentdetails),
    path('update/<int:id>/',views.update),
    path('update_view/',views.update_view),
    path('deletestu/<int:id>/',views.deletestu),
    path('search/',views.search,name='search'),
    path('teacherdetails/',views.teacherdetails),
    path('addteacher/',views.addteacher),
    # api urls esme hum add kr sakte hai
    path('reg/',RegistrationViewSet.as_view()),
    # esme saare show hoge
    path('show/',RegistrationShowViewSet.as_view()),
    path('regcr/',CourseViewSet.as_view()),
    path('showcr/',CourseShowViewSet.as_view()),
    path('regstu/',AddstudentViewSet.as_view()),
    path('showstu/',AddstudentShowViewSet.as_view()),
    path('showid/<int:pk>/',RegistrationIdViewSet.as_view()),
    path('showupdate/<int:pk>/',RegistrationUpdateViewSet.as_view()),
    path('deluser/<int:pk>/',RegistrationDeleteViewSet.as_view())
    
]
