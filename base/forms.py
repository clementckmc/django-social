from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from .models import Post, Reply

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'How are you doing?', 'cols': 20, 'rows': 5})
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
