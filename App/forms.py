from django import forms

from App.models import Contact


class ContactForm(forms.ModelForm ):
    name = forms.CharField(max_length=100)
    contact_info = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = 'name', 'contact_info', 'message'

    def is_submitted(self):
        return True