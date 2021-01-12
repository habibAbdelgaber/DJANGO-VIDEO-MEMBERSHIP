from django import forms
from .models import PostComment




class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'placeholder': 'Leave a comment...',
        'rows': 3,
        'cols': 40
    }))
    class Meta:
        model = PostComment
        fields = ('content',)