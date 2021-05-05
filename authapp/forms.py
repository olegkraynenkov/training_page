from django.contrib.auth.forms import AuthenticationForm

from .models import AuthUser


class AuthUserLoginForm(AuthenticationForm):
    class Meta:
        model = AuthUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(AuthUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'