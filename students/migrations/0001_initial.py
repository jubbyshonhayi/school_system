from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
                ('enrollment_date', models.DateField(db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='schools.school')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'indexes': [models.Index(fields=['school', 'last_name', 'first_name'], name='students_st_school__416d6b_idx'), models.Index(fields=['school', 'email'], name='students_st_school__f3c3ce_idx'), models.Index(fields=['school', 'enrollment_date'], name='students_st_school__7f77b6_idx')],
                'constraints': [models.UniqueConstraint(fields=('school', 'email'), name='unique_student_email_per_school')],
            },
        ),
    ]
