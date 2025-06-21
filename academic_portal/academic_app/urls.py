from django.urls import path,include
from academic_app.views import StudentAttendenceList, TeacherAttendanceList
from academic_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('students/',views.StudentList, name='students'),
    path('teachers/', views.TeacherList, name='teachers'),
    path('courses/', views.CoursesList, name='courses'),
    path('batches/', views.BatchesList, name='batches'),
  
    path('studentattendence/', StudentAttendenceList.as_view(), name='StudentAttendence'),
    path('teacherattendance/', TeacherAttendanceList.as_view(), name='TeacherAttendance'),
    path('subjects/', views.SubjectsList, name='subjects'),
    path('classrooms/',views.ClassroomList, name='classrooms'),
    path('lessonplans/', views.LessonPlanListView.as_view(), name='lessonplan_list'),
    path('lessonplans/<int:pk>/', views.LessonPlanDetailView.as_view(), name='lessonplan_detail'),
    path('lessonplans/add/', views.LessonPlanCreateView.as_view(), name='lessonplan_add'),
    path('timetable/', views.show_timetable, name='timetable_display'),
]