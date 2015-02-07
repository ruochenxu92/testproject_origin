from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from task.models import Article

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)

    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        pass


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'body',  'pub_date')
