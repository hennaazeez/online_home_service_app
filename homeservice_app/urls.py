from django.urls import path

from homeservice_app import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("",views.index,name="index"),
    path("index1", views.index1, name="index1"),
    path("loginpage", views.loginpage, name="loginpage"),
    path("registration",views.registration,name="registration"),
    path("reg1", views.reg1, name="reg1"),
    path("workers", views.workers, name="workers"),
    path("customers", views.customers, name="customers"),
    path("customer_registration",views.customer_registration,name="customer_registration"),
    path("workers_registration", views.workers_registration, name="workers_registration"),
    path("workers_data", views.workers_data, name="workers_data"),
    path("workers1", views.workers1, name="workers1"),
    path("base", views.adminbase, name="base"),
    path("customerbase", views.customerbase, name="customerbase"),
    path("customer_data", views.customer_data, name="customer_data"),
    path("workerbase", views.workerbase, name="workerbase"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("delete_it/<int:id>/", views.delete_it, name="delete_it"),
    path("update/<int:id>/", views.update, name="update"),
    path("feedbackform", views.feedbackform, name="feedbackform"),
    path("view",views.view,name="view"),
    path("feedbacks", views.feedbacks, name="feedbacks"),
    path("reply_feedback/<int:id>/", views.reply_feedback, name="reply_feedback"),
    path("schedule", views.schedule, name="schedule"),
    path("view_schedule", views.view_schedule, name="view_schedule"),
    path("delete_schedule/<int:id>/", views.delete_schedule, name="delete_schedule"),
    path("customer_view_schedule", views.customer_view_schedule, name="customer_view_schedule"),
    path("worker_view_schedule", views.worker_view_schedule, name="worker_view_schedule"),
    path("view_workers", views.view_workers, name="view_workers"),
    path("work_add", views.work_add, name="work_add"),
    path("work_view", views.work_view, name="work_view"),
    path("delete_work_view/<int:id>/", views.delete_work_view, name="delete_work_view"),
    path("update_work_view/<int:id>/", views.update_work_view, name="update_work_view"),
    path("take_appointment/<int:id>/", views.take_appointment, name="take_appointment"),
    path("view_appointment", views.view_appointment, name="view_appointment"),
    path("admin_view_appointment", views.admin_view_appointment, name="admin_view_appointment"),
    path("approve_appointment/<int:id>/", views.approve_appointment, name="approve_appointment"),
    path("reject_appointment/<int:id>/", views.reject_appointment, name="reject_appointment"),
    path("worker_view_appointment", views.worker_view_appointment, name="worker_view_appointment"),
    path("worker_view_appointment", views.worker_view_appointment, name="worker_view_appointment"),
    path("bill", views.bill, name="bill"),
    path("view_bill", views.view_bill, name="view_bill"),
    path("customer_view_payment", views.customer_view_payment, name="customer_view_payment"),

]
