from django.conf.urls import url
from restaurant.utils import views

urlpatterns = [
    url(r'^$', views.home_page_view),
    url(r'^search/$', views.search_view, name="search"),
    url(r'^collections/all/$', views.collection_list_view),
    url(r'^collections/(\d+)/$', views.collection_restaurant_list_view),
    url(r'^categories/(\d+)/$', views.category_list_view),
    url(r'^restaurant/add/$', views.add_restaurant, name="add_restaurant")

]
