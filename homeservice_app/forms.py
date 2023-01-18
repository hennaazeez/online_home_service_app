from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput, TimeInput

from homeservice_app.models import Complaints, register1, register, Login, schedule_add, work, Bill


class DateInput(forms.DateInput):
    input_type = 'date'



class TimeInput(forms.TimeInput):
    input_type = 'time'



class Login_form(UserCreationForm):
    class Meta:
        model=Login
        fields = ("username","password1","password2")


class register_form(forms.ModelForm):
    class Meta:
        model = register
        fields ='__all__'
        exclude=('user',)


class register_form1(forms.ModelForm):
    class Meta:
        model = register1
        fields ='__all__'
        exclude=('user',)

class FeedbackForm(forms.ModelForm):


    class Meta:
        model = Complaints
        fields = ('feedback',)

class ScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput, )
    end_time = forms.TimeField(widget=TimeInput, )

    class Meta:
        model = schedule_add
        fields = ( 'date','start_time','end_time')

class work_form(forms.ModelForm):

    class Meta:
        model=work
        fields='__all__'


class AddBill(forms.ModelForm):
    # name = forms.ModelChoiceField(queryset=Customers.objects.filter(role='customer'))

    class Meta:
        model = Bill
        exclude = ('status','paid_on')





