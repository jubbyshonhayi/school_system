from django.db import models


class Student(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'

    school = models.ForeignKey('schools.School', on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=Gender.choices)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    enrollment_date = models.DateField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        indexes = [
            models.Index(fields=['school', 'last_name', 'first_name']),
            models.Index(fields=['school', 'email']),
            models.Index(fields=['school', 'enrollment_date']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['school', 'email'], name='unique_student_email_per_school')
        ]

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
