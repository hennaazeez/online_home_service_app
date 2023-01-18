from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
from homeservice_app.forms import Login_form, register_form, register_form1, FeedbackForm, ScheduleForm, work_form, \
    AddBill
from homeservice_app.models import register, Login, register1, Complaints, schedule_add, work, Take_appointment, Bill


def home(request):
    return render(request,"home.html")
def index(request):
    return render(request,"index.html")
def index1(request):
    return render(request,"index1.html")
def loginpage(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pass")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("base")
            if user.is_customer:
                return redirect("customerbase")
            if user.is_workers:
                return redirect("workerbase")
        else:
            messages.info(request,"no user found")

    return render(request,"login.html")
def registration(request):
    return render(request,"registration.html")
def reg1(request):
    return render(request,"reg1.html")
def workers(request):
    return render(request,"worker/workers.html")
def customers(request):
    return render(request,"customers.html")

def customer_registration(request):
    form1 = Login_form()
    form2 =register_form1()
    if request.method =="POST":
        form1 = Login_form(request.POST)
        form2 = register_form1(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_customer = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect('loginpage')
    return render(request,"customer/customers.html",{'form1': form1,'form2':form2})


def workers_registration(request):
    form1 = Login_form()
    form2 =register_form()
    if request.method =="POST":
        form1 = Login_form(request.POST)
        form2 = register_form(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_workers = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect('loginpage')
    return render(request,"worker/workers.html",{'form1': form1,'form2':form2})

def workers_data(request):
    data=register.objects.all
    print(data)
    return render(request,"worker/workers_data.html",{"data":data})

def workers1(request):
    return render(request,"workers1.html")

def adminbase(request):
    return render(request,"admin/admin base.html")

def customerbase(request):
    return render(request,"customer/customer base.html")

def workerbase(request):
    return render(request,"worker/worker base.html")

def customer_data(request):
    data=register1.objects.all
    print(data)
    return render(request,"customer/customer_data.html",{"data":data})

def delete(request,id):
    wm=register.objects.get(id=id)
    wm.delete()
    return redirect("workers_data")

def delete_it(request,id):
    wm=register1.objects.get(id=id)
    wm.delete()
    return redirect("customer_data")

def update(request,id):
    homeservice = register.objects.get(id=id)
    form = register_form(instance=homeservice)
    if request.method == 'POST':
        form =register_form(request.POST,instance=homeservice)
        if form.is_valid():
            form.save()
            return redirect('workers_data')

    return render(request,'update.html',{'form':form})

def feedbackform(request):
    form = FeedbackForm()
    u = request.user
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            return redirect("feedbackform")

    return render(request,'feedback.html',{"form":form})

def view(request):
    data = Complaints.objects.filter(user=request.user)
    print(data)
    return render(request, "view.html", {"data": data})

def feedbacks(request):
    n = Complaints.objects.all()
    return render(request,"admin/feedbacks.html",{"feedbacks":n})

def reply_feedback(request,id):
    feedback = Complaints.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.save()
        messages.info(request, 'reply send for complaints')
        return redirect('view')
    return render(request,'reply_feedback.html',{'feedback':feedback})


def schedule(request):
    form = ScheduleForm()
    # u = request.user
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.worker=register.objects.get(user=request.user)
            obj.save()
            return redirect("view_schedule")

    return render(request, "worker/schedule.html", {"form": form})

def view_schedule(request):
    n = schedule_add.objects.all()
    return render(request, "admin/view_schedule.html",{"view_schedule":n})

def delete_schedule(request,id):
    wn = schedule_add.objects.get(id=id)
    wn.delete()
    return redirect("view_schedule")

def customer_view_schedule(request):
    n = schedule_add.objects.all()
    return render(request, "customer/customer_view_schedule.html",{"customer_view_schedule":n})

def worker_view_schedule(request):
    n = schedule_add.objects.all()
    return render(request, "worker/worker_view_schedule.html",{"worker_view_schedule":n})

def view_workers(request):
    data = register.objects.all()
    return render(request,"customer/view_workers.html",{"data":data})

def work_add(request):
    form = work_form()
    if request.method=='POST':
        form=work_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("work_view")
    return render(request,'admin/work_add.html',{'form':form})

def work_view(request):
    data=work.objects.all()
    return render(request,'admin/work_view.html',{'data':data})

def delete_work_view(request,id):
    wn = work.objects.get(id=id)
    wn.delete()
    return redirect("work_view")


def update_work_view(request,id):
    a = work.objects.get(id=id)
    form = work_form(instance=a)
    if request.method == 'POST':
        form = work_form(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('work_view')

    return render(request,'admin/update_work_view.html',{'form':form})

def take_appointment(request,id):
    s = schedule_add.objects.get(id=id)
    c = register1.objects.get(user=request.user)
    app = Take_appointment.objects.filter(user=c,schedule=s)
    if app.exists():
        messages.info(request,"already booked")
        return redirect('customer_view_schedule')
    else:
        if request.method == 'POST':
            obj = Take_appointment()
            obj.user = c
            obj.schedule = s
            obj.save()
            messages.info(request,"appointment is successfully booked")
            return redirect('view_appointment')
    return render(request,"customer/take_appointment.html",{"s":s})

def view_appointment(request):
    # c = register1.objects.get(user=request.user)
    a = Take_appointment.objects.all
    return render(request,"customer/view_appointment.html",{"app":a})


def admin_view_appointment(request):
    a = Take_appointment.objects.all
    return render(request,"admin/admin_view_appointment.html",{"app":a})

def approve_appointment(request, id):
    n = Take_appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request, 'Appointment confirmed')
    return redirect('admin_view_appointment')

def reject_appointment(request, id):
    n = Take_appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('admin_view_appointment')

def worker_view_appointment(request):
    # c = register1.objects.get(user=request.user)
    a = Take_appointment.objects.filter(status=1)

    return render(request,"worker/worker_view_appointment.html",{"app":a})

def bill(request):
    form = AddBill()
    if request.method == 'POST':
        form = AddBill(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_bill')

    return render(request,'admin/generate_bill.html', {'form': form})



def view_bill(request):
    bill = Bill.objects.all()
    print(bill)
    return render(request, 'admin/view_payment_details.html', {'bill': bill})



def customer_view_payment(request):
    u = register1.objects.get(user =request.user)
    bill = Bill.objects.all()
    print(bill)
    return render(request, 'customer/customer_view_payment.html',{'a':a})



