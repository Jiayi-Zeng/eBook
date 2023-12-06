# eBook/forms.py

from allauth.account.forms import LoginForm

class YourLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(YourLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'yourclass'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'yourclass'})