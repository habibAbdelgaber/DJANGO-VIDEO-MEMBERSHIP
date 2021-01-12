from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=250)
    img = models.ImageField(upload_to='images/', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

 
    def __str__(self):
        return self.title

    

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    
    def get_like_url(self):
        return reverse('blog:like', kwargs={'slug': self.slug})

    
    # @property
    # def comments(self):
    #     return self.comment_set.all()
        
    # @property
    # def get_comment_count(self):
    #     return self.comment_set.all().count()

    @property
    def get_view_count(self):
        return self.postview_set.all().count()

    
    @property
    def get_like_count(self):
        return self.likepost_set.all().count()


class PostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.email

class PostView(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

class LikePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
