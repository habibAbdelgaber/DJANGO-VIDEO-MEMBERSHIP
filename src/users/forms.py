from django.contrib.auth import forms 
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from django import forms as dj_forms

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import get_user_model


User = get_user_model()

class CancelSubscriptionForm(dj_forms.Form):
    hidden = dj_forms.HiddenInput()

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError(self.error_messages["duplicate_username"])
  