from django import forms
from .models import ContactModel, bp_products, bp_users

MATEN = (('s', 'S - 15cm-16cm'),('m', 'M - 16.5cm-18cm'), ('l', 'L - 18cm-20cm'), ('xl', 'XL - 20cm-22cm'))

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = ('voornaam', 'email', 'onderwerp', 'text')

class ShoppingForm(forms.ModelForm):
    quantity = forms.IntegerField()
    maat = forms.ChoiceField(choices=MATEN)
    pr_prijs = forms.CharField(max_length=200, widget=forms.HiddenInput())
    pr_naam = forms.CharField(max_length=200, widget=forms.HiddenInput())

    class Meta:
        model = bp_products
        fields = ['pr_prijs', 'pr_naam']

class Login(forms.ModelForm):

    class Meta:
        model = bp_users
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class Registreren(forms.ModelForm):

    class Meta:
        model = bp_users
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
        }
