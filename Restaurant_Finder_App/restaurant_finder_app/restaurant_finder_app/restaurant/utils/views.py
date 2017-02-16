from django.shortcuts import render
from restaurant.models import Restaurant, Collection, Category, MenuImage, RestaurantTiming, Cuisine
import operator
from django.db.models import Q
from functools import reduce
from restaurant.utils.forms import AddRestaurantForm, MenuForm, RestaurantTimingsForm
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.


def search_view(request):
    query = request.GET.get('search_query')
    if len(query) > 0:
        if query:
            query_list = query.split()
            restaurant_list = Restaurant.objects.filter(
                reduce(operator.and_,
                       (Q(restaurant_name__icontains=search_text) for search_text in query_list))
            )

        if not restaurant_list:
            collection_list = Collection.objects.filter(
                reduce(operator.and_,
                       (Q(collection_name__icontains=search_text) for search_text in query_list))
            )
            for collection in collection_list:
                restaurant_list = collection.restaurant.all()

        if not restaurant_list:
            category_list = Category.objects.filter(
                reduce(operator.and_,
                       (Q(name__icontains=search_text) for search_text in query_list))
            )
            for category in category_list:
                restaurant_list = category.restaurant.all()

        if not restaurant_list:
            cuisine_list = Cuisine.objects.filter(
                reduce(operator.and_,
                       (Q(cuisine_name__icontains=search_text) for search_text in query_list))
            )
            for cuisine in cuisine_list:
                restaurant_list = cuisine.restaurant.all()

        context = {'restaurant_list': restaurant_list, }
        return render(request, 'restaurant_list.html', context)


def home_page_view(request):
    restaurant_list = Restaurant.objects.all()
    collection_list = Collection.objects.all()
    category_list = Category.objects.all()
    trending_restaurant_collection = Collection.objects.get(pk=6)
    trending_restaurants = trending_restaurant_collection.restaurant.all()
    context = {'restaurant_list': restaurant_list,
               'collection_list': collection_list[:4],
               'category_list': category_list,
               'trending_restaurant_list': trending_restaurants[:4]}
    return render(request, 'home_page.html', context)


def collection_list_view(request):
    try:
        collections = Collection.objects.all()
    except Collection.DoesNotExist:
        raise Http404("Collection does not exist")

    context = {'collection_list': collections}
    return render(request, 'collection_list.html', context)


def collection_restaurant_list_view(request, collection_id):
    try:
        collection = Collection.objects.get(pk=collection_id)
    except Collection.DoesNotExist:
        raise Http404("Collection does not exist")

    context = {'collection': collection,
               'restaurant_list': collection.restaurant.all}
    return render(request, 'collection_restaurant_list.html', context)


def category_list_view(request, category_id):
    try:
        categories = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")

    context = {'restaurant_list': categories.restaurant.all}
    return render(request, 'restaurant_list.html', context)

def add_restaurant(request):
    MenuFormSet = modelformset_factory(
        MenuImage, form=MenuForm, extra=4, fields=('menu_image',),)
    RestaurantTimingFormSet = modelformset_factory(
        RestaurantTiming, form=RestaurantTimingsForm, extra=7, fields=('working_days', 'start_time', 'end_time',),)
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST, request.FILES)
        menuformset = MenuFormSet(request.POST, request.FILES,
                                  queryset=MenuImage.objects.none(), prefix='menu')
        restaurantTimingsformset = RestaurantTimingFormSet(request.POST, request.FILES,
                                                           queryset=RestaurantTiming.objects.none(), prefix='restaurant_timing')
        if form.is_valid() and menuformset.is_valid() and restaurantTimingsformset.is_valid():
            categories = form.cleaned_data['category']
            restaurant = form.save(commit=True)

            for category in categories:
                category.restaurant.add(restaurant)

            for menuform in menuformset:
                if menuform.is_valid():
                    image = menuform.cleaned_data.get('menu_image')
                    if not image is None :
                        picture = MenuImage(
                            restaurant=restaurant, menu_image=image)
                        picture.save()

            for restaurantTimings in restaurantTimingsformset:
                if restaurantTimings.is_valid():
                    working_days = restaurantTimings.cleaned_data.get(
                        'working_days')
                    start_time = restaurantTimings.cleaned_data.get(
                        'start_time')
                    end_time = restaurantTimings.cleaned_data.get('end_time')
                    if not working_days is None and not start_time is None and not end_time is None:
                        timing = RestaurantTiming(
                        restaurant=restaurant, working_days=working_days, start_time=start_time, end_time=end_time)
                        timing.save()

            return HttpResponseRedirect('/')
        else:  # invalid case
            print (form.errors)
            print(menuformset.errors)
            print(restaurantTimingsformset.errors)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddRestaurantForm()
        menuformset = MenuFormSet(
            queryset=MenuImage.objects.none(), prefix='menu')
        restaurantTimingsformset = RestaurantTimingFormSet(
            queryset=RestaurantTiming.objects.none(), prefix='restaurant_timing')

    return render(request, 'add_restaurant.html', {'form': form, 'menuformset': menuformset, 'restaurantTimingsformset': restaurantTimingsformset})


def view_restaurant(request, restaurant_id):
    try:
        restaurant_detail = Restaurant.objects.get(pk=restaurant_id)
        now = datetime.datetime.now()
        isOpened = False
        open_time = ''
        for timing in restaurant_detail.restaurant_timing.all():
            if(timing.working_days.day.lower() == now.strftime("%A").lower()):
                if now.time() > timing.start_time and now.time() < timing.end_time:
                    isOpened = True
                    open_time = "Today " + \
                        str(timing.start_time) + " - " + str(timing.end_time)
                else:
                    isOpened = False
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")

    context = {'restaurant': restaurant_detail,
               'isOpened': isOpened, 'open_time': open_time}
    return render(request, 'restaurant_detail.html', context)
