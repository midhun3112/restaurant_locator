from django import forms
from authentication.models import User, UserProfile
from django.utils.translation import gettext as _
from restaurant.models import Restaurant, Category


class AddRestaurantForm(forms.ModelForm):
    restaurant_name = forms.CharField(widget=forms.TextInput(
        attrs={'size': '100', 'class': 'form-control'}), required=True, max_length=255)
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(), required=True)
    restaurant_image = forms.ImageField(
        label='Select A Image For The Restaurant', required=True)
    restaurant_image_thumbnail = forms.ImageField(
        label='Select A Thumbnail Image For The Restaurant', required=True)
    address_1 = forms.CharField(widget=forms.TextInput(
        attrs={'size': '100', 'class': 'form-control'}), required=True, max_length=500)
    address_2 = forms.CharField(widget=forms.TextInput(
        attrs={'size': '100', 'class': 'form-control'}), required=True, max_length=500)
    locality = forms.CharField(widget=forms.TextInput(
        attrs={'size': '100', 'class': 'form-control'}), required=True, max_length=255)
    city = forms.CharField(widget=forms.TextInput(
        attrs={'size': '100', 'class': 'form-control'}), required=True, max_length=255)
    state = forms.CharField(widget=forms.TextInput(
        attrs={'size': '100', 'class': 'form-control'}), required=True, max_length=255)
    pincode = forms.IntegerField(required=True)
    country = forms.CharField(widget=forms.TextInput(
        attrs={'size': '100', 'class': 'form-control'}), required=True, max_length=255)
    phone_number_1 = forms.CharField(widget=forms.TextInput(
        attrs={'size': '100', 'class': 'form-control'}), required=True, max_length=15)
    phone_number_2 = forms.CharField(widget=forms.TextInput(
        attrs={'size': '100', 'class': 'form-control'}), required=False, max_length=15)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Restaurant

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        fields = ('restaurant_name', 'category', 'restaurant_image', 'restaurant_image_thumbnail', 'address_1',
                  'address_2', 'locality', 'city', 'state', 'pincode', 'country', 'phone_number_1', 'phone_number_2')

    # def clean_email(self):
    #     try:
    #         user = User.objects.get(email__iexact=self.cleaned_data['email'])
    #     except User.DoesNotExist:
    #         return self.cleaned_data['email']
    #     raise forms.ValidationError(
    # _("The email already exists. Please try another one. If you forgot
    # the password please try the forgot password option to recover your
    # password"))

    # def clean(self):
    #     if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
    #         if self.cleaned_data['password1'] != self.cleaned_data['password2']:
    #             raise forms.ValidationError(
    #                 _("The two password fields did not match."))
    #     return self.cleaned_data
