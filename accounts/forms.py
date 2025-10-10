

"""

    For both new forms, we are using the Meta class to override the default fields by
setting the model to our CustomUser and using the default fields via
Meta.fields which includes all default fields. To add our custom age field, we
simply tack it on at the end, and it will display automatically on our future
signup page.

"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email", "age")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
