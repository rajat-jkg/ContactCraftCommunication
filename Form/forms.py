
from django import forms
from .models import ContactForm

class AddForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['form_name', 'form_css']
        labels = {
            'form_name': 'Form Name',
            'form_css': 'Custom CSS'
        }
        widgets = {
            'form_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Form Name', 'id:': 'form_name_input'}),
            'form_css': forms.Textarea(attrs={'class': 'form-control' , 'placeholder': 'Enter the desired CSS here. Leave blank if you want the default CSS. You can also edit the CSS later', 'id': 'form_css_input' }),
        }
