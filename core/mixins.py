from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class SchoolScopedMixin(LoginRequiredMixin):
    """Tenant isolation: only allow school-scoped users to access school data."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            raise PermissionDenied('Superusers should use Django admin for school management.')
        if not getattr(request.user, 'is_school_user', False):
            raise PermissionDenied('A school assignment is required.')
        return super().dispatch(request, *args, **kwargs)

    def get_school(self):
        return self.request.user.school


class SchoolQuerysetMixin(SchoolScopedMixin):
    model = None

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(school=self.get_school())
