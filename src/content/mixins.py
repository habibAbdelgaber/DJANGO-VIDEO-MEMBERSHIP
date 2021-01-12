from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Course


class CoursePermissionMixins:
    def dispatch(self, request, *args, **kwargs):
        course = get_object_or_404(Course, slug=self.kwargs['slug'])
        subscription = request.user.subscription
        pricing_tier = subscription.pricing
        if not pricing_tier in course.pricing_tiers.all():
            messages.info(request, 'You do not have a permission to access this course. Please upgrade to start')
            return redirect('content:course-list')
        return super().dispatch(request, *args, **kwargs)
