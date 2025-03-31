from django import forms
from django.core.mail import send_mail

from blog.models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("author",)

    pub_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"},),
    )

    def clean(self):
        super().clean()
        send_mail(
            subject="Новая публикация!!!",
            message=f"Новая публикация \"{self.cleaned_data.get('title')}\" "
            f"с названием {self.cleaned_data['title']}",
            from_email="moriarty@blogicum.not",
            recipient_list=["admin@blogicum.not"],
            fail_silently=True,
        )
