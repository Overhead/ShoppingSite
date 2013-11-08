from django.conf.urls import patterns, url
from shopping import views


urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^new/', views.create_shopping_item, name='create_shopping_item'),
                       )

