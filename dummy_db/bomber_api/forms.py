from django import forms
from .models import Parent

# form for password field in model Parent
class ParentForm(forms.ModelForm):
    class Meta:
        model: Parent
        widgets = {
        'password': forms.PasswordInput(),
    }
