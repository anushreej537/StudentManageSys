from django.urls import path
from app import views
from app.api.api import RegistrationViewSet
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
    path('reg/',RegistrationViewSet.as_view())
      
]
