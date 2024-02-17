from django import forms
from django.contrib.auth.forms import UserCreationForm


from event_app.models import Login, Teacher, Student, Club, event, Notification, Feedback, Join_request


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ("username","password1","password2")

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ("user_1",)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ("user_2",)
class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'
class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'

class EventForm(forms.ModelForm):
    event_date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)
    class Meta:
        model = event
        fields = '__all__'
        exclude = ("club_1",)
class NotificationForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Notification
        fields = '__all__'
class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = '__all__'
        exclude = ("reply","user",)
class FeedbackReplyForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields='__all__'
        # exclude=("user",)

class Join_requestForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)
    class Meta:
        model=Join_request
        fields='__all__'






