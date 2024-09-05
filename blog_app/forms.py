from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

    def __init__(self, *args, **kwargs):
        # Extract user from kwargs if present
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super().save(commit=False)
        if self.user:
            post.author = self.user
        if commit:
            post.save()
        return post
