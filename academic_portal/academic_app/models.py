from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    classroom = models.ForeignKey('ClassRoom', on_delete=models.CASCADE, null=True, blank=True) 
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE)
    def __str__(self):
       return f"{self.name} - [{self.classroom.name}]"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    joining_date = models.DateField()
    qualification = models.CharField(max_length=200, blank=True, null=True)
    departement = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

   
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
   
    def __str__(self):
        return self.name

class Batch(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    courses = models.ManyToManyField(Course, related_name='batches') 
    def __str__(self):
      course_names = ", ".join(course.name for course in self.courses.all())
      return f"{self.name} - [{course_names}]"


    
class TimeTable(models.Model):
    days_of_week = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
 ]

    subject = models.ForeignKey('Subject',on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=days_of_week)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.ForeignKey('ClassRoom', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.classroom.name} - {self.subject.name}  ({self.day_of_week})"
    

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
   

    def __str__(self):
        return f"{self.name} - {self.teacher.name}"
    
class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave')],
        default='Present')
    classroom = models.ForeignKey('ClassRoom', on_delete=models.CASCADE, null=True, blank=True) 
   


    def __str__(self):
       return f"{self.student.name} - {self.date} - {self.get_status_display()}"

class TeacherAttendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent')],
        default='Present')  # True for present, False for absent


    def __str__(self):
      return f"{self.teacher.name} - {self.date} - {self.get_status_display()}"
    

class LessonPlan(models.Model):
    title = models.CharField(max_length=200)
    classroom = models.ForeignKey('ClassRoom', on_delete=models.CASCADE, null=True, blank=True) 
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    planned_date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.teacher.name}"

class ClassRoom(models.Model):
    name = models.CharField(max_length=100)  # e.g. "Class A", "Maths 1A"
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name='classrooms')
    def __str__(self):
        return f"{self.name} - {self.course.name} ({self.batch.name})"