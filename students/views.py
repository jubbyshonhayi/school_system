from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from core.mixins import SchoolQuerysetMixin

from .forms import StudentForm
from .models import Student


class StudentListView(SchoolQuerysetMixin, ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '').strip()
        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
                | Q(email__icontains=query)
                | Q(phone__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '').strip()
        return context


class StudentDetailView(SchoolQuerysetMixin, DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'


class StudentCreateView(SchoolQuerysetMixin, CreateView):
    model = Student
    template_name = 'students/student_form.html'
    form_class = StudentForm
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        form.instance.school = self.get_school()
        messages.success(self.request, 'Student added successfully.')
        return super().form_valid(form)


class StudentUpdateView(SchoolQuerysetMixin, UpdateView):
    model = Student
    template_name = 'students/student_form.html'
    form_class = StudentForm
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        form.instance.school = self.get_school()
        messages.success(self.request, 'Student updated successfully.')
        return super().form_valid(form)


class StudentDeleteView(SchoolQuerysetMixin, DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        messages.success(self.request, 'Student deleted successfully.')
        return super().form_valid(form)
