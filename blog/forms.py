from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Add Comment Form to Posts
    
    **Context**
    ``CommentForm``
        An instance of :form:`post.CommentForm`.
    """
    class Meta:
        model = Comment
        fields = ('body',)