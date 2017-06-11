from django import forms
from .models import ContactModel, ShopCart

MATEN = (('s', 'S - 15cm-16cm'),('m', 'M - 16.5cm-18cm'), ('l', 'L - 18cm-20cm'), ('xl', 'XL - 20cm-22cm'))

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = ('voornaam', 'email', 'onderwerp', 'text')

class ShoppingForm(forms.Form):
    maat = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=MATEN
    )

    q = forms.IntegerField()
