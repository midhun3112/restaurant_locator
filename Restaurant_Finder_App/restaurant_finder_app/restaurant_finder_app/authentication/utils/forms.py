from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm ,PasswordResetForm,SetPasswordForm
from django import forms
from authentication.models import User, UserProfile
from django.utils.translation import gettext as _

class UserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """
    def __init__(self, *args, **kargs):
        super(UserCreationForm, self).__init__(*args, **kargs)
        if 'username' in self.fields:
            del self.fields['username']

    class Meta:
        model = User
        fields = ("email",)

class UserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    def __init__(self, *args, **kargs):
        super(UserChangeForm, self).__init__(*args, **kargs)
        if 'username' in self.fields:
            del self.fields['username']

    class Meta:
        model = User
        fields = ("email",)

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'required': True, 'max_length': 30, 'placeholder': "Enter your email id", 'style': 'width:84%'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True, 'required': True,'render_value': False, 'placeholder': "Enter your password", 'style': 'width:84%'}))

# If you don't do this you cannot use Bootstrap CSS
class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'required': True, 'max_length': 30, 'placeholder': "Enter your email id", 'style': 'width:84%'}))

# If you don't do this you cannot use Bootstrap CSS
class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'required': True, 'required': True,'render_value': False, 'placeholder': "Enter your password", 'style': 'width:84%'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'required': True, 'required': True,'render_value': False, 'placeholder': "Re-Enter your password", 'style': 'width:84%'}))

class RegistrationForm(forms.Form):
 
    firstname = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'max_length': 30, 'placeholder': "Enter your first name", 'style': 'width:84%'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'max_length': 30, 'placeholder': "Enter your last name", 'style': 'width:84%'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'required': True, 'max_length': 30, 'placeholder': "Enter your email id", 'style': 'width:84%'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'required': True, 'required': True,'render_value': False, 'placeholder': "Enter your password", 'style': 'width:84%'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'required': True, 'required': True,'render_value': False, 'placeholder': "Re-Enter your password", 'style': 'width:84%'}))
 
    def clean_email(self):
        try:
            user = User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_("The email already exists. Please try another one. If you forgot the password please try the forgot password option to recover your password"))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birth_date', 'genre', 'address1', 'address2', 'postal_code', 'state', 'country', 'is_owner')