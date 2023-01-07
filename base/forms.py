from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Reply, User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

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
        fields = ['username', 'bio']

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
