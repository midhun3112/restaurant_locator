from django.conf.urls import url
from restaurant import views

urlpatterns = [
  url(r'$',views.home_page_view),
  url(r'^restaurant/restaurant_list$',views.restaurant_list_view)

]