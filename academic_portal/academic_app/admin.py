from django.contrib import admin
from .models import Student, Batch, Course, Teacher, TimeTable, Subject, StudentAttendance, TeacherAttendance, LessonPlan, ClassRoom

# Register your models here.
admin.site.register(Student)
admin.site.register(Batch)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(StudentAttendance)
admin.site.register(TeacherAttendance)
admin.site.register(LessonPlan)
admin.site.register(ClassRoom)
admin.site.register(TimeTable)