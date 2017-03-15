from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from emailauth.models import EmailAuthUser

class EmailAuthUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(EmailAuthUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = EmailAuthUser
        fields = ("email",)

class EmailAuthUserChangeForm():
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(EmailAuthUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = EmailAuthUser
