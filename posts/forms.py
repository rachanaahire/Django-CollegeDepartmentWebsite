from django import forms
from posts.models import *


class PostForm(forms.ModelForm):


    class Meta:
        model = PostStudent
        fields = [
            "title",
            "content",
        ]


