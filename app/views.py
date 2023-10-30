from django.shortcuts import render,redirect
import re
from django.db.models import Q
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.http import HttpResponse
def courses(request):
    course_obj = Course.objects.all()
    return render(request,'courses.html',{'course_obj':course_obj})

def addcourse(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        fees = request.POST.get('fees')
        duration = request.POST.get('duration')
        if Course.objects.filter(course_name=course_name).exists():
            messages.error(request,'already exists')
        else:
            Course.objects.create(course_name=course_name,fees=fees,duration=duration)
            messages.success(request,'course added successfully')
            return redirect('/courses/')

def dashboard(request):
    obj = Course.objects.all().count()
    return render(request,'dashboard.html',{'obj':obj})

def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def addstudent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobileno = request.POST.get('mobileno')
        address = request.POST.get('address')
        degree = request.POST.get('degree')
        college = request.POST.get('college')
        total_amount = request.POST.get('totalamount')
        paid_amount = request.POST.get('paidamount')
        due_amount = request.POST.get('dueamount')
        course_id = request.POST.get('course')
        stu_course = Course.objects.get(id=course_id)
        if Addstudent.objects.filter(email=email).exists():
            messages.error(request,'email already exist')
            return redirect('/studentdetails/')
        elif Addstudent.objects.filter(mobileno=mobileno).exists():
            messages.error(request,'mobile num already exist')
            return redirect('/studentdetails/')
        else:
            Addstudent.objects.create(name=name,email=email,mobileno=mobileno,address=address,
                                      degree=degree,college=college,total_amount=total_amount,
                                      paid_amount=paid_amount,due_amount=due_amount,course=stu_course)
            return redirect('/studentdetails/')

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.error(request,'email already exist')
            return redirect('/signup/')
        else:
            # if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$",password):
            User.objects.create(name=name,email=email,password=password)
            messages.error(request,'user registered successfully')
            return redirect('/')
            # else:
                # messages.error(request,'create strong password')
                # return redirect('/signup/')
        
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # if User.objects.filter(email=email).exists():
        #     obj = User.objects.get(email=email)
        #     userpassword = obj.password
        #     if check_password(userpassword,password):
        #         return redirect('/dashboard/')
        #     else:
        #         messages.error(request,'password not correct')
        #         return redirect('/')
        # else:
        #     messages.error(request,'email not register')
        #     return redirect('/')
        if User.objects.filter(email=email).exists():
            messages.error(request,'email match')
            if User.objects.filter(password=password).exists():
                messages.error(request,' password match')
                return redirect('/dashboard/')
            else:
                messages.error(request,' pas not')
                return redirect('/')
        else:
            messages.error(request,' email not')
    else:
        messages.success(request,'Successfully login')

def studentdetails(request):
    allcourse = Course.objects.all()
    allstu = Addstudent.objects.all()
    return render(request,'studentdetails.html',{'allcourse':allcourse,'allstu': allstu})

def update(request,id):
    data = Addstudent.objects.get(id=id)
    allcourses = Course.objects.all()
    return render(request,'update.html',{'data':data, 'allcourses':allcourses})

def update_view(request,):
    id = request.POST.get('uid')
    name = request.POST.get('name')
    email = request.POST.get('email')
    mobileno = request.POST.get('mobileno')
    address = request.POST.get('address')
    degree = request.POST.get('degree')
    college = request.POST.get('college')
    total_amount = request.POST.get('totalamount')
    paid_amount = request.POST.get('paidamount')
    due_amount = request.POST.get('dueamount')
    course_id = request.POST.get('course')
    stu_course = Course.objects.get(id=course_id)
    Addstudent.objects.filter(id=id).update(name=name,email=email,mobileno=mobileno,address=address,
                                             degree=degree,college=college,total_amount=total_amount,
                                             paid_amount=paid_amount,due_amount=due_amount,course=stu_course)
    return redirect('/studentdetails/')


def deletestu(request,id):
    Addstudent.objects.get(id=id).delete()
    return redirect('/studentdetails/')


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(name__icontains=q) | Q(email__icontains=q)) | Q(mobileno__icontains=q)
        allstu = Addstudent.objects.filter(multiple_q)
        print(multiple_q)
    else:
        allstu = Addstudent.objects.all()
    context = {'allstu':allstu}
    return render(request,'studentdetails.html',context)


def teacherdetails(request):
    allcourse = Course.objects.all()
    allteacher = Addteacher.objects.all()
    return render(request,'teacherdetails.html',{'allcourse':allcourse,'allteacher':allteacher})

def addteacher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobileno = request.POST.get('mobileno')
        work= request.POST.get('work')
        course_id = request.POST.get('course')
        stu_course = Course.objects.get(id=course_id)
        if Addteacher.objects.filter(email=email).exists():
            messages.error(request,'email already exist')
            return redirect('/teacherdetails/')
        elif Addteacher.objects.filter(mobileno=mobileno).exists():
            messages.error(request,'mobile num already exist')
            return redirect('/teacherdetails/')
        else:
            Addteacher.objects.create(name=name,email=email,mobileno=mobileno,
                                      work=work,course=stu_course)
            return redirect('/teacherdetails/')
    