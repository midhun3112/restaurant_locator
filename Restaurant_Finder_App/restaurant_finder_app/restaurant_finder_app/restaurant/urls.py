from django.conf.urls import url
from restaurant.utils import views

urlpatterns = [
  url(r'^$',views.home_page_view),
  url(r'^restaurant/(\d+)/$',views.restaurant_list_view)

]