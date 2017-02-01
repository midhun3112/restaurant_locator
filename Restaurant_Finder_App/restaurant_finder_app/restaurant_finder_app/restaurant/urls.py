from django.conf.urls import url
from restaurant.utils import views

urlpatterns = [
  url(r'^$',views.home_page_view),
  url(r'^collections/(\d+)/$',views.collection_list_view),
  url(r'^categories/(\d+)/$',views.category_list_view)

]