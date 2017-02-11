from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Restaurant(models.Model):
    restaurant_name = models.CharField(
        max_length=255,
    )
    restaurant_image = models.ImageField(
        upload_to='images/restaurant_pic/',
        default='images/restaurant_pic/no-name.jpg'
    )
    restaurant_thumbnail_image = models.ImageField(
        upload_to='images/restaurant_pic/thumbnails/',
        default='images/restaurant_pic/thumbnails/no-name.jpg'
    )
                    
    class Meta:
        default_related_name = 'restaurant'

    def __str__(self):
        return '{}'.format(self.restaurant_name)


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
