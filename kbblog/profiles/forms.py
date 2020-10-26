from django import forms
from ckeditor.widgets import CKEditorWidget

from profiles.models import Post

#User
from django.contrib.auth.models import User

class PostClientForm(forms.ModelForm):
    post_content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ['post_title', 'post_content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['post_title'].widget.attrs.update({
            'class': 'posting-write-card__input posting-write-card__input--title',
            'placeholder': 'title'
        })

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'transition-input login-card__input login-card__input--id'})
        self.fields['password'].widget.attrs.update({
            'class': 'transition-input login-card__input login-card__input--pw',
            'type': 'password'
        })