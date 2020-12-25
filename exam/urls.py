from django.urls import path
from . import views

app_name = 'exam'
urlpatterns = [
    path('', views.index, name='index'),
    path('loginStudent/', views.loginStudent, name='loginStudent'),
    path('loginTeacher/', views.loginTeacher, name='loginTeacher'),
    # path('studentLogin/', views.studentLogin, name='studentLogin'),
    path('showGrade',views.showGrade),
    path('queryStudent/',views.queryStudent),
    path('startExam/',views.startExam),
    path('calGrade/',views.calGrade),
]
