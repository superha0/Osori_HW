from django import forms

from .models import Post, Comment

# post writing form
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


# comment writing form
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)