from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Post, PostComment, PostView, LikePost
from .forms import CommentForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    # model = Post
    queryset = Post.objects.all()
    # template_name = 'blog/post_detail.html'


    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('blog:detail', slug=post.slug)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
        })
        return context

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)
        return object


def like_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = LikePost.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('blog:detail', slug=slug)
    LikePost.objects.create(user=request.user, post=post)
    return redirect('blog:detail', slug=slug)
