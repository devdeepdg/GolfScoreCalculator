from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from .models import Course


class inputScoreForm(forms.Form):

    courseChoice = forms.ModelChoiceField(queryset=Course.objects.all())

    handicap = forms.IntegerField()
    score = SimpleArrayField(forms.IntegerField())
    #score1 = forms.IntegerField()
    #score2 = forms.IntegerField()
    #score3 = forms.IntegerField()
    #score4 = forms.IntegerField()
    #score5 = forms.IntegerField()
    #score6 = forms.IntegerField()
    #score7 = forms.IntegerField()
    #score8 = forms.IntegerField()
    #score9 = forms.IntegerField()
    #score10 = forms.IntegerField()
    #score11 = forms.IntegerField()
    #score12 = forms.IntegerField()
    #score13 = forms.IntegerField()
    #score14 = forms.IntegerField()
    #score15 = forms.IntegerField()
    #score16 = forms.IntegerField()
    #score17 = forms.IntegerField()
    #score18 = forms.IntegerField()


class addCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'city', 'country', 'strokeIndex', 'par')
