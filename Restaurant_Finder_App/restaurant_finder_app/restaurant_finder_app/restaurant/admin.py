from django.contrib import admin

# Register your models here.
from .models import Restaurant, WeekDay, RestaurantTiming, Collection, Category, EstablishmentType, Cuisine, CostForTwo

admin.site.register(Restaurant)
admin.site.register(WeekDay)
admin.site.register(RestaurantTiming)
admin.site.register(Collection)
admin.site.register(Category)
admin.site.register(EstablishmentType)
admin.site.register(Cuisine)
admin.site.register(CostForTwo)
