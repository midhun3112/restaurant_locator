from django import forms
from authentication.models import User, UserProfile
from django.utils.translation import gettext as _
from restaurant.models import Restaurant, Category, MenuImage, WeekDay, RestaurantTiming
from django.forms.formsets import BaseFormSet


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
    is_pure_veg = forms.BooleanField(required=False)
    is_credits_cards_accepted = forms.BooleanField(required=False)
    is_buffet_offered = forms.BooleanField(required=False)
    is_wifi_offered = forms.BooleanField(required=False)
    is_alcohol_served = forms.BooleanField(required=False)
    has_outdoor_seating = forms.BooleanField(required=False)

    class Meta:
        model = Restaurant

        fields = ('restaurant_name', 'category', 'restaurant_image', 'restaurant_image_thumbnail', 'address_1',
                  'address_2', 'locality', 'city', 'state', 'pincode', 'country', 'phone_number_1', 'phone_number_2', 'is_pure_veg', 'is_credit_cards_accepted', 'is_buffet_offered', 'is_wifi_offered', 'is_alcohol_served', 'has_outdoor_seating',)


class MenuForm(forms.ModelForm):
    menu_image = forms.ImageField(label='Menu Image')

    class Meta:
        model = MenuImage
        fields = ('menu_image', )


class RestaurantTimingsForm(forms.ModelForm):
    working_days = forms.ModelChoiceField(
        queryset=WeekDay.objects.all(), empty_label="(Select Week Day)", required=True)
    start_time = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M'), required=True)
    end_time = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M'), required=True)

    class Meta:
        model = RestaurantTiming
        fields = ('working_days', 'start_time', 'end_time')
