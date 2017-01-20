from django.contrib import admin

# Register your models here.
from .models import Restaurant, WeekDay, RestaurantTiming, Collection, Category

admin.site.register(Restaurant)
admin.site.register(WeekDay)
admin.site.register(RestaurantTiming)
admin.site.register(Collection)
admin.site.register(Category)
