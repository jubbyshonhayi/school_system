from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from students.models import Student


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_superuser or not getattr(user, 'is_school_user', False):
            context['student_count'] = 0
            context['recent_students'] = []
            return context

        queryset = Student.objects.filter(school=user.school)
        context['student_count'] = queryset.count()
        context['recent_students'] = queryset.order_by('-created_at')[:5]
        return context
