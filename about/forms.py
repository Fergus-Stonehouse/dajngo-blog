from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Add CollaborateForm to About
    
    **Context**
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`.
        
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')