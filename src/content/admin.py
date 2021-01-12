from django.contrib import admin
from .models import Course, Video, Pricing, Subscription

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


class PricingAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Course, CourseAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Subscription)


# admin.site.site_header = 'Membership Subscription'
# admin.site.site_title = 'Video membership website'