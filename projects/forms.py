from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        exclude = ('id', 'vote_total', 'vote_ratio', 'created')


        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # a for loop to iterate over all the fields in the form 
        # and set the widget if all the fields are shared same widget

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input'}
            )

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input', 'placeholder': 'Project title'}
        # )

        # self.fields['description'].widget.attrs.update(
        #     {'class': 'input', 'placeholder': 'Description'}
        # )