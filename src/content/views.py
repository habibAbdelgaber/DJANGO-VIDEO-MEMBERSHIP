from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Course, Video
from .mixins import CoursePermissionMixins


class CourseListView(ListView):
    queryset = Course.objects.all()
    template_name = 'content/course_list.html'

class CourseDetailView(LoginRequiredMixin, DetailView):
    queryset = Course.objects.all()
    template_name = 'content/course_detail.html'


class VideoDetailView(LoginRequiredMixin, CoursePermissionMixins, DetailView):
    template_name = 'content/video_detail.html'

    def get_object(self):
        video = get_object_or_404(Video, slug=self.kwargs['video_slug'])
        return video

    def get_queryset(self):
        course = get_object_or_404(Course, slug=self.kwargs['slug'])
        return course.videos.all()

    # def get_context_data(self):
        
    


