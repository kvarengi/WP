from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class AddWalletForm(forms.Form):
    wallet = forms.CharField(max_length=50)

class RemoveWalletForm(forms.Form):
    wallet = forms.ChoiceField()

class MakeBetForm(forms.Form):
    token_a = forms.ChoiceField()
    token_b = forms.ChoiceField()
    bet_size = forms.FloatField()
    duration = forms.TimeField()
    percent = forms.FloatField()


class DepositForm(forms.Form):
    ammount = forms.FloatField()
    payment_method = forms.ChoiceField()


class SellForm(forms.Form):
    ammount = forms.FloatField()
    source = forms.ChoiceField()

