
from .models import Comments
from django import forms


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('rollno', 'name', 'comment_body')