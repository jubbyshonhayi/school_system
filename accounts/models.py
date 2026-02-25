from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    SCHOOL_USER = 'SCHOOL_USER', 'School User'


class User(AbstractUser):
    school = models.ForeignKey(
        'schools.School',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='users',
    )
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.SCHOOL_USER, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=['school', 'role']),
        ]

    @property
    def is_school_user(self) -> bool:
        return self.role == UserRole.SCHOOL_USER and self.school_id is not None
