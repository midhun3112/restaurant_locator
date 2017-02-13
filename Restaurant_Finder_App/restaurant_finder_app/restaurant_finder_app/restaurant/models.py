from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
# Create your models here.


class Restaurant(models.Model):
    restaurant_name = models.CharField(
        max_length=255,
        blank=False
    )
    restaurant_image = models.ImageField(
        upload_to='images/restaurant_pic/',
        default='images/restaurant_pic/restaurant_image.jpg'
    )
    restaurant_image_thumbnail = models.ImageField(
        upload_to='images/restaurant_pic/thumbnail/',
        default='images/restaurant_pic/thumbnail/restaurant_image_thumbnail.jpg'
    )
    address_1 = models.CharField(
        max_length=500,
        blank=False
    )
    address_2 = models.CharField(
        max_length=500,
        blank=False
    )
    locality = models.CharField(
        max_length=255,
        blank=False
    )
    city = models.CharField(
        max_length=255,
        blank=False
    )
    state = models.CharField(
        max_length=255,
        blank=False
    )
    pincode = models.IntegerField()
    country = models.CharField(
        max_length=255,
        blank=False
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # validators should be a list
    phone_number_1 = models.CharField(
        max_length=15,
        validators=[phone_regex],
        blank=False)
    phone_number_2 = models.CharField(
        max_length=15,
        validators=[phone_regex],
        blank=True
    )
    is_pure_veg = models.BooleanField(default=False)
    is_credit_cards_accepted = models.BooleanField(default=False)
    is_buffet_offered = models.BooleanField(default=False)
    is_wifi_offered = models.BooleanField(default=False)
    is_alcohol_served = models.BooleanField(default=False)
    has_outdoor_seating = models.BooleanField(default=False)

    class Meta:
        default_related_name = 'restaurant'

    def __str__(self):
        return '{}'.format(self.restaurant_name)


class EstablishmentType(models.Model):
    type_of_establishment = models.CharField(
        max_length=500,
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, null=True)

    class Meta:
        default_related_name = 'establishment_type'
        verbose_name = _('EstablishmentType')
        verbose_name_plural = _('EstablishmentTypes')

    def __str__(self):
        return self.type_of_establishment


class Cuisine(models.Model):
    cuisine_name = models.CharField(
        max_length=500,
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, null=True)

    class Meta:
        default_related_name = 'cuisine'
        verbose_name = _('Cuisine')
        verbose_name_plural = _('Cusines')

    def __str__(self):
        return self.cuisine_name


class CostForTwo(models.Model):
    cost_for_two = models.CharField(
        max_length=500,
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, null=True)

    class Meta:
        default_related_name = 'cost_for_two'
        verbose_name = _('CostForTwo')
        verbose_name_plural = _('CostForTwo')

    def __str__(self):
        return self.cost_for_two


class WeekDay(models.Model):
    day = models.CharField(
        max_length=255,
    )

    class Meta:
        default_related_name = 'week_day'
        verbose_name = _('WeekDay')
        verbose_name_plural = _('WeekDays')

    def __str__(self):
        return self.day


class RestaurantTiming(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, null=True)
    working_days = models.ForeignKey(
        WeekDay, on_delete=models.CASCADE, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        default_related_name = 'restaurant_timing'
        verbose_name = _('Restaurant Timing')
        verbose_name_plural = _('Restaurant Timings')

    def __str__(self):
        return '%s - %s - %s - %s' % (self.restaurant.restaurant_name,
                                      self.working_days.day,
                                      self.start_time,
                                      self.end_time)


class Collection(models.Model):
    restaurant = models.ManyToManyField(Restaurant)
    collection_name = models.CharField(
        max_length=255,
    )
    collection_image_thumbnail = models.ImageField(
        upload_to='images/collections_pic/thumbnails/',
        default='images/collections_pic/thumbnails/no-name.jpg'
    )
    collection_image = models.ImageField(
        upload_to='images/collections_pic/',
        default='images/collections_pic/no-name.jpg'
    )
    collection_description = models.CharField(
        max_length=2000,
    )

    class Meta:
        default_related_name = 'collections'

    def __str__(self):
        return '%s' % (self.collection_name)


class Category(models.Model):
    restaurant = models.ManyToManyField(Restaurant)
    name = models.CharField(
        max_length=255,
    )
    category_image = models.ImageField(
        upload_to='images/categories_pic/',
        default='images/categories_pic/no-name.jpg'
    )

    class Meta:
        default_related_name = 'categories'
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return '%s' % (self.name)


class MenuImage(models.Model):
    menu_image = models.ImageField(
        upload_to='images/menu_pic/',
        default='images/menu_pic/menu.jpg'
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, null=True)

    class Meta:
        default_related_name = 'menu_image'
        verbose_name = _('MenuImage')
        verbose_name_plural = _('MenuImages')

    # def __unicode__(self):
    #     return unicode(self.image_location)
