from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from event_app.forms import LoginRegister, TeacherForm, StudentForm, ClubForm, EventForm, NotificationForm, \
    FeedbackForm, FeedbackReplyForm, Join_requestForm
from event_app.models import Student, Teacher, Club, event, Notification, Feedback, Join_request, Join


def home(request):
    return render(request,'index.html')
def new(request):
    return render(request,'dashb.html')

def teacher_login(request):
    Login_form = LoginRegister()
    Teacher_form = TeacherForm()
    if request.method == "POST":
        Login_form = LoginRegister(request.POST)
        Teacher_form = TeacherForm(request.POST)

        if Login_form.is_valid() and Teacher_form.is_valid():
            user2=Login_form.save(commit=False)
            user2.is_teacher=True
            user2.save()
            user1=Teacher_form.save(commit=False)
            user1.user_1=user2
            user1.save()
            return redirect('login_view')
    return render(request,'form.html',{'Login_form':Login_form,'Teacher_form':Teacher_form})

def student_login(request):
    Login_form = LoginRegister()
    Student_form = StudentForm()
    if request.method=="POST":
        Login_form=LoginRegister(request.POST)
        Student_form=StudentForm(request.POST)

        if Login_form.is_valid() and Student_form.is_valid():
            user2=Login_form.save(commit=False)
            user2.is_student=True
            user2.save()
            user1=Student_form.save(commit=False)
            user1.user_2=user2
            user1.save()
            return redirect('login_view')
    return render(request,'form2.html',{'Login_form':Login_form,'student_form':Student_form})
def ad_base(request):
    return render(request,'admintemplate/base.html')



def teach_base(request):
    data = Teacher.objects.get(user_1=request.user)
    return render(request, 'teacher/base.html', {'data': data})



def stu_base(request):
    data =Student.objects.get(user_2=request.user)
    return render(request,'student/base.html',{'data':data})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('ad_base')
            elif user.is_teacher:
                return redirect('teach_base')
            elif user.is_student:
                return redirect('stu_base')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'login.html')

def stuview(request):
    data = Student.objects.all()
    return render(request,'admintemplate/studentview.html',{'data1':data})

def teachview(request):
    data = Teacher.objects.all()
    return render(request,'admintemplate/teacherview.html',{'data2':data})

def studelt(request,id):
    if request.method == 'POST':
        data=Student.objects.get(id=id)
        data.delete()
        return redirect("stuview")

def teachdelt(request,id):
    if request.method == 'POST':
        data=Teacher.objects.get(id=id)
        data.delete()
        return redirect("teachview")

def stuupdate(request,id):
    stu= Student.objects.get(id=id)
    form=StudentForm(instance=stu)
    if request.method == 'POST':
        form=StudentForm(request.POST,instance=stu)
        if form.is_valid():
            form.save()
            return redirect('stuview')
    return render(request,'admintemplate/stuupdate.html',{'form1':form})

def teachupdate(request,id):
    tea= Teacher.objects.get(id=id)
    form=TeacherForm(instance=tea)
    if request.method == 'POST':
        form=TeacherForm(request.POST,instance=tea)
        if form.is_valid():
            form.save()
            return redirect('teachview')
    return render(request,'admintemplate/teachupdate.html',{'form2':form})

def club(request):
    Club_form = ClubForm()
    if request.method == "POST":
        Club_form = ClubForm(request.POST,request.FILES)
        if Club_form.is_valid():
            Club_form.save()
            return redirect('ad_base')
    return render(request,'admintemplate/club.html',{"form3":Club_form})

def clubview(request):
    data=Club.objects.all()
    return render(request,'admintemplate/clubview.html',{'data':data})
def clubdelt(request,id):
    if request.method == "POST":
        data=Club.objects.get(id=id)
        data.delete()
        return redirect("clubview")
def clubupdate(request,id):
    clu=Club.objects.get(id=id)
    form=ClubForm(instance=clu)
    if request.method == "POST":
        form=ClubForm(request.POST,request.FILES,instance=clu)
        if form.is_valid():
            form.save()
            return redirect("clubview")
    return render(request,"admintemplate/clubupdate.html",{"form":form})

def viewclub(request):
    data=Club.objects.all()
    return render(request,'teacher/viewclub.html',{'data':data})

def stuclub_view(request):
    data=Club.objects.all()
    return render(request,'student/stuclubview.html',{'data':data})

def club_event(request,id):
    data=Club.objects.get(id=id)

    form=EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            d=form.save(commit=False)
            d.club_1=data
            d.save()

    return render(request,"teacher/events.html",{"form":form})

def view_event(request):
    data = event.objects.all()
    return render(request,"teacher/eventview.html",{"data":data})
def event_update(request,id):
    eve = event.objects.get(id=id)
    form = EventForm(instance=eve)
    if request.method == "POST":
        form = EventForm(request.POST,instance=eve)
        if form.is_valid():
            form.save()
    return render(request,'teacher/eventupdate.html',{"form":form})

def eventdelt(request,id):
    if request.method == "POST":
        data=event.objects.get(id=id)
        data.delete()
        return redirect("view_event")

def notification(request):
    not_form = NotificationForm()
    if request.method == "POST":
        not_form = NotificationForm(request.POST)
        if not_form.is_valid():
            not_form.save()
    return render(request,'admintemplate/notification.html',{"form":not_form})
def notadm_view(request):
    data = Notification.objects.all()
    return render(request,'admintemplate/notview.html',{"data":data})

def notstu_view(request):
    data = Notification.objects.all()
    return render(request, 'student/notview.html', {"data": data})

def nottea_view(request):
    data = Notification.objects.all()
    return render(request, 'teacher/notview.html', {"data": data})

def feed_back(request):
    form = FeedbackForm()
    user_1=request.user
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user=user_1
            data.save()
    return render(request,"student/feedback.html",{"form":form})
def feedstd_view(request):
    u=request.user.id
    data = Feedback.objects.filter(user=u)
    return render(request, 'student/feedview.html', {"data": data})
def feedadm_view(request):
    data = Feedback.objects.all()
    return render(request, 'admintemplate/fbview.html', {"data": data})

def reply_feed(request,id):
    feedback =Feedback.objects.get(id=id)

    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('feedadm_view')
    return render(request, 'admintemplate/reply.html', {'feedback': feedback})

def Reply_View(request):
    stu=request.user
    print(stu)
    data=Feedback.objects.filter(user=stu)
    return render(request,'student/replystd.html',{"data":data})
def Joinreq_teacher(request):
    join_form = Join_requestForm()
    if request.method == "POST":
        join_form = Join_requestForm(request.POST)
        if join_form.is_valid():
            join_form.save()
    return render(request, 'teacher/joinreq.html', {"form": join_form})
def joinreq_view(request):
    data=Join_request.objects.all()
    return render(request,"teacher/joinview.html",{"data":data})
def joinreq_update(request,id):
    req = Join_request.objects.get(id=id)
    form = Join_requestForm(instance=req)
    if request.method == "POST":
        form = Join_requestForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
    return render(request, 'teacher/requestupdate.html', {"form": form})
def request_delt(request,id):
    if request.method == "POST":
        data=Join_request.objects.get(id=id)
        data.delete()
def joinstd_view(request):
    data=Join_request.objects.all()
    return render(request,"student/joinstdview.html",{"data":data})

# def join_page(request,id):
#     join =Join_request.objects.get(id=id)
#
#     return render(request, 'student/join.html', {'join': join})
def send_req(request,id):
    show=Join_request.objects.get(id=id)
    std=request.user

    u=Student.objects.get(user_2=std)

    v=Join.objects.filter(user=u,approve=show)

    if v.exists():
        messages.info(request,'you have already requested to join')
        return redirect('joinstd_view')
    else:
        if request.method == "POST":
            obj=Join()
            obj.user=u
            obj.approve=show
            obj.save()
            messages.info(request,'join request send successfully')
            # return redirect()
        return render(request,'student/join.html',{'join':show })

def sendreq_view(request):
    data=Join.objects.all()
    return render(request,'teacher/stureqview.html',{'data':data})

def teaapprove(request,id):
    data=Join.objects.get(id=id)
    if request.method == "POST":
        data.status=1
        data.save()
        return redirect("sendreq_view")


def teareject(request,id):
    data=Join.objects.get(id=id)
    if request.method == "POST":
        data.status=2
        data.save()
        return redirect("sendreq_view")

@login_required(login_url='login_view')
def logout_view(request):
    logout(request)
    return redirect('login_view')

























