from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.ig_today,name='igToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/article$', views.new_post, name='new-post')
]
