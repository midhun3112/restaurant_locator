from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Restaurant(models.Model):
	restaurant_name = models.CharField(
			max_length = 255,
		)
	restaurant_image = models.ImageField(
		upload_to = 'images/restaurant_pic/',
		default = 'restaurant_pic/images/no-name.jpg'
		)

	class Meta:
		default_related_name = 'restaurant'

	def __str__(self):
		return '{}'.format(self.restaurant_name)

class WeekDay(models.Model):
	day = models.CharField(
			max_length = 255,
		)

	class Meta:
		default_related_name = 'week_day'

	def __str__(self):
		return self.day
	
class RestaurantTiming(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
	working_days = models.ForeignKey(WeekDay, on_delete=models.CASCADE, null=True)
	start_time = models.TimeField()
	end_time = models.TimeField()

	class Meta:
		default_related_name = 'restaurant_timing'

	def __str__(self):
		return '%s - %s - %s - %s' % (self.restaurant.restaurant_name, self.working_days.day,  self.start_time , self.end_time)

class Collection(models.Model):
	restaurant = models.ManyToManyField(Restaurant)
	collection_name = models.CharField(
			max_length = 255,
		)

	class Meta:
		default_related_name = 'collections'

	def __str__(self):
		return '%s' % (self.collection_name)

class Category(models.Model):
	restaurant = models.ManyToManyField(Restaurant)
	name = models.CharField(
			max_length = 255,
		)

	class Meta:
		default_related_name = 'categories'
		verbose_name = _('category')
		verbose_name_plural = _('categories')

	def __str__(self):
		return '%s' % (self.name)

