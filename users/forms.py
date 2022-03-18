from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # a for loop to iterate over all the fields in the form 
        # and set the widget if all the fields are shared same widget

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input'}
            )


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        # fields = "__all__"
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # a for loop to iterate over all the fields in the form 
        # and set the widget if all the fields are shared same widget

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input'}
            )