from django import forms

from .models import Post


class PostForm(forms.ModelForm):


    class Meta:


        model = Post
        fields = ['first_name', 'last_name', 'rating', 'post']
