from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        labels = {
            'mobile': 'Mobile No.',
        }

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select here'
        # required field remover
        self.fields['email'].required = False
        self.fields['mobile'].required = False
