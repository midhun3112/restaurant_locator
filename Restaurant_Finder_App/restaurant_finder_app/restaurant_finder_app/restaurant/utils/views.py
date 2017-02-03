from django.shortcuts import render
from restaurant.models import Restaurant, Collection, Category

# Create your views here.


def home_page_view(request):
    restaurant_list = Restaurant.objects.all()
    collection_list = Collection.objects.all()
    category_list = Category.objects.all()
    context = {'restaurant_list': restaurant_list,
               'collection_list': collection_list[:4],
               'category_list': category_list}
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
