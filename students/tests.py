from django.test import TestCase
from django.urls import reverse

from accounts.models import User, UserRole
from schools.models import School
from .models import Student


class TenantIsolationTests(TestCase):
    def setUp(self):
        self.school1 = School.objects.create(name='A School', email='a@example.com')
        self.school2 = School.objects.create(name='B School', email='b@example.com')
        self.user1 = User.objects.create_user(username='user1', password='pass1234', school=self.school1, role=UserRole.SCHOOL_USER)
        self.user2 = User.objects.create_user(username='user2', password='pass1234', school=self.school2, role=UserRole.SCHOOL_USER)
        self.student = Student.objects.create(
            school=self.school1,
            first_name='John',
            last_name='Doe',
            date_of_birth='2010-01-01',
            gender='M',
            email='john@example.com',
            phone='123',
            enrollment_date='2020-01-01',
        )

    def test_user_cannot_access_other_school_student(self):
        self.client.login(username='user2', password='pass1234')
        response = self.client.get(reverse('students:detail', args=[self.student.pk]))
        self.assertEqual(response.status_code, 404)
