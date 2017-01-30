from django.shortcuts import render
from restaurant.models import Restaurant, Collection, Category

# Create your views here.

def home_page_view(request):
	restaurant_list = Restaurant.objects.all()
	collection_list = Collection.objects.all()
	category_list = Category.objects.all()
	context = {'restaurant_list': restaurant_list, 'collection_list': collection_list, 'category_list': category_list}
	return render(request, 'home_page.html', context)

def restaurant_list_view(request, collection_id):
	try:
		print(collection_id)
		collections = Collection.objects.get(pk=collection_id)
	except Collection.DoesNotExist:
		raise Http404("Collection does not exist")

	context = {'restaurant_list': collections.restaurant.all}
	return render(request, 'restaurant_list.html', context)