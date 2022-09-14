from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    def save(self, commit=True):
        instance = super(SignupForm, self).save(commit=False)
        instance.is_superuser = False
        instance.is_staff = True
        instance.is_active = True
        if commit:
            instance.save()
        return instance

    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "password"]


class SigninForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
