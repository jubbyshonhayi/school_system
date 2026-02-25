from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'email',
            'phone',
            'enrollment_date',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
        }
