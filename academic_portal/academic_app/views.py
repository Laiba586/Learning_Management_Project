from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course,Batch, Student, Teacher, TimeTable, Subject,ClassRoom, StudentAttendance, TeacherAttendance, LessonPlan
import math
from django.utils import timezone
from django.views import View
from datetime import date, datetime
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
import openpyxl
from collections import defaultdict

# Create your views here.
def index(request):
    return render(request, "academic_app/index.html")
def StudentList(request):
       students = Student.objects.all()
       return render(request, 'academic_app/student.html', {'students': students})

def TeacherList(request):
    teachers = Teacher.objects.all()
    return render(request, "academic_app/teacher.html", {'teachers': teachers})

def CoursesList(request):
    allcourses = Course.objects.all()


    return render(request, 'academic_app/corses.html', {'allcourses': allcourses})
 

def BatchesList(request):

   batches = Batch.objects.all().order_by('-start_date')  # Recent batches first
   return render(request, 'academic_app/baches.html', {'batches': batches})

class StudentAttendenceList(View):
    def get(self, request):
        selected_date = request.GET.get('date')
        if selected_date:
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
        else:
            selected_date = date.today()

        students = Student.objects.select_related('classroom').all()

        attendances = StudentAttendance.objects.filter(date=selected_date)
        present_ids = [a.student.id for a in attendances if a.status == 'Present']

        return render(request, 'academic_app/studentattendence.html', {
            'students': students,
            'selected_date': selected_date,
            'present_ids': present_ids,
        })

    def post(self, request):
        selected_date = request.POST.get('date')
        selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()

        students = Student.objects.select_related('classroom').all()

        for student in students:
            is_present = f'present_{student.id}' in request.POST
            attendance, created = StudentAttendance.objects.get_or_create(
                student=student,
                date=selected_date,
                defaults={'status': 'Present' if is_present else 'Absent'}
            )
            if not created:
                attendance.status = 'Present' if is_present else 'Absent'
                attendance.save()

        return redirect(f'/studentattendence/?date={selected_date}')

class TeacherAttendanceList(View):
    def get(self, request):
        selected_date = request.GET.get('date')
        if selected_date:
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
        else:
            selected_date = date.today()

        teachers = Teacher.objects.all()

        attendances = TeacherAttendance.objects.filter(date=selected_date)
        present_ids = [a.teacher.id for a in attendances if a.status == 'Present']

        return render(request, 'academic_app/teacherattendence.html', {
            'teachers': teachers,
            'selected_date': selected_date,
            'present_ids': present_ids,
        })

    def post(self, request):
        selected_date = request.POST.get('date')
        selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()

        teachers = Teacher.objects.all()

        for teacher in teachers:
            is_present = f'present_{teacher.id}' in request.POST
            attendance, created = TeacherAttendance.objects.get_or_create(
                teacher=teacher,
                date=selected_date,
                defaults={'status': 'Present' if is_present else 'Absent'}
            )
            if not created:
                attendance.status = 'Present' if is_present else 'Absent'
                attendance.save()

        return redirect(f'/teacherattendence/?date={selected_date}')




def SubjectsList(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects
    }
    return render(request, "academic_app/subjects.html", context)

   

def ClassroomList(request):
    classrooms = ClassRoom.objects.all()
    return render(request, 'academic_app/classroom.html', {'classrooms': classrooms})



class LessonPlanListView(ListView):
    model = LessonPlan
    template_name = 'academic_app/lessonplan_list.html'
    context_object_name = 'lessonplans'

class LessonPlanDetailView(DetailView):
    model = LessonPlan
    template_name = 'academic_app/lessonplan_detail.html'
    context_object_name = 'lessonplan'

class LessonPlanCreateView(CreateView):
    model = LessonPlan
    fields = ['title', 'classroom', 'subject', 'teacher', 'content', 'planned_date']
    template_name = 'academic_app/lessonplan_form.html'
    success_url = reverse_lazy('lessonplan_list')



def show_timetable(request):
    timetable_entries = TimeTable.objects.select_related('classroom', 'subject', 'teacher')

    schedule = defaultdict(lambda: defaultdict(list))  # schedule[class_name][day] = [entries]

    # Step 1: group entries by classroom
    class_data = defaultdict(list)
    for entry in timetable_entries:
        class_name = entry.classroom.name if entry.classroom else "Unassigned"
        class_data[class_name].append(entry)

    # Step 2: for each class, copy its entries across all days
    for class_name, entries in class_data.items():
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
            schedule[class_name][day] = entries  # same entries in each day

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    return render(request, 'academic_app/timetable_display.html', {
        'schedule': dict(schedule),
        'days': days,
    })