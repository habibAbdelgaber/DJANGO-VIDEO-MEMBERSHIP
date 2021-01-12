from django.contrib import admin
from django.forms import Textarea
from django.db import models
from tinymce.widgets import TinyMCE
from .models import Post, PostComment, PostView, LikePost



class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    prepopulated_fields = {'slug': ('title', )}

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


# class CommentAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': Textarea(attrs={
#             'rows': 1,
#             'cols': 30
#         })},
#     }

admin.site.register(Post, PostAdmin)
admin.site.register(PostComment)
admin.site.register(PostView)
admin.site.register(LikePost)
